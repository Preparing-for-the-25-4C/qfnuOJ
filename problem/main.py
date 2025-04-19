# main_async.py

import asyncio
import logging
import time
import sys
from src import extract_text_between_tags, getTopicSurface, saveKeywords
from volcenginesdkarkruntime import AsyncArk

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)


class AsyncProcessor:
    def __init__(self, api_key, model, max_concurrent=10):
        self.client = AsyncArk(api_key=api_key)
        self.model = model
        self.semaphore = asyncio.Semaphore(max_concurrent)
        self.baseprompt = None

    async def init_prompt(self):
        with open('prompt.txt', 'r', encoding='utf8') as f:
            self.baseprompt = f.read()
        logging.info("提示词模板加载成功")

    async def process_item(self, index):
        async with self.semaphore:
            iteration_start = time.time()
            logging.info(f"【开始处理】索引 {index}")

            try:
                # 异步获取题面
                TopicSurface = await asyncio.to_thread(getTopicSurface, index)
                PROMPT = self.baseprompt.replace("{{题面}}", TopicSurface)

                # 使用批量接口
                logging.info(f"发送批量请求[索引{index}]")
                api_start = time.time()

                # 修改点：使用batch_chat接口
                completion = await self.client.batch_chat.completions.create(
                    model=self.model,  # 确认模型名称是否符合批量要求
                    messages=[{"role": "user", "content": PROMPT}],
                )

                api_duration = time.time() - api_start
                logging.info(f"收到响应[索引{index}] 耗时 {api_duration:.2f}秒")

                # 处理响应
                if not completion.choices:
                    logging.warning(f"索引 {index} 无有效结果")
                    return

                res = completion.choices[0].message.content
                extracted = extract_text_between_tags(res)

                if not extracted:
                    logging.error(f"索引 {index} 内容提取失败")
                    return

                await asyncio.to_thread(saveKeywords, index, extracted)

                iteration_duration = time.time() - iteration_start
                logging.info(f"【完成处理】索引 {index} 总耗时 {iteration_duration:.2f}秒")

            except Exception as e:
                logging.error(f"处理失败[索引{index}]: {str(e)}", exc_info=True)


async def main():
    try:
        processor = AsyncProcessor(
            api_key = "",
            model="",  # 确认这是批量端点ID
            max_concurrent=10
        )
        await processor.init_prompt()

        total_items = 540
        start_time = time.time()
        logging.info(f"开始处理 {total_items} 个任务，并发数10")

        tasks = [processor.process_item(i) for i in range(total_items)]

        # 分批处理防止内存溢出
        batch_size = 100
        for i in range(0, len(tasks), batch_size):
            await asyncio.gather(*tasks[i:i + batch_size])
            logging.info(f"已完成批次 {i // batch_size + 1}/{(len(tasks) - 1) // batch_size + 1}")

        total_duration = time.time() - start_time
        logging.info(f"全部完成，总耗时 {total_duration / 60:.2f} 分钟")

    except Exception as e:
        logging.error(f"初始化失败: {str(e)}", exc_info=True)


if __name__ == "__main__":
    if sys.platform == 'win32':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    asyncio.run(main())