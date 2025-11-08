from translation import auto_translate
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set HF_TOKEN from environment variable
os.environ["HF_TOKEN"] = os.getenv("HF_TOKEN")


output_lang = "vi"

prompt = lambda content: f'''

You are a translator for the Vietnamese translation team. You are tasked with translating the following texts into Vietnamese. You must follow these instructions:
- Translate the texts into Vietnamese, while keeping the original formatting (either Markdown, MDX or HTML)
- Inside code blocks, translate the comments but leave the code as-is; If the code block contains quite plain texts, you MUST provide the translation in <details> tag
- Do not translate inline code, the URLs and file paths
- If the term is abbreviated, keep the original term and provide the translation in parentheses for the first time it appears in the text
- If there are any slag or funny joke in english, keep it (do not translate) and give an explanation so Vietnamese reader can understand
- Use "ta", "mình, "chúng ta", "chúng mình", "các bạn" as pronouns

KEEP THESE TERMS (DO NOT TRANSLATE, do NOT add translation in parentheses): Hugging Face, LeRobot, Transformer, LeRobotDataset, Metadata
For these terms, use the pre-defined translation:
- Onboarding: Làm quen
- Course: Khóa học
- Unit: Chương
- Bonus Unit: Chương bổ trợ
- Module: Mô-đun
- Lesson ...: Bài ...
- Quick Quiz: Kiểm tra nhanh
- Model: Mô hình
- Dataset: Bộ dữ liệu
- Q&A: Hỏi và Đáp
- Hands-on: Thực hành
- Challenge: Bài tập lớn
- Training: Huấn luyện
- Machine learning: Học máy

Here is an example:
- Original text: This free course will take you on a journey, **from classical robotics to modern learning-based approaches**, in understanding, implementing, and applying machine learning techniques to real robotic systems.
- Translation: Khóa học miễn phí này sẽ đưa bạn vào một hành trình, **từ robot cổ điển đến các phương pháp hiện đại dựa trên học máy**, để hiểu, triển khai và áp dụng các kỹ thuật học máy vào các hệ thống robot thực tế.

Here is another example:
- Original text: For more information about robot learning, check out the [Hugging Face documentation](https://huggingface.co/docs/lerobot) and explore our [LeRobot datasets](https://huggingface.co/datasets/lerobot) to get started with your own projects.
- Translation: Để biết thêm thông tin về robot learning, hãy xem [tài liệu Hugging Face](https://huggingface.co/docs/lerobot) và khám phá [bộ dữ liệu LeRobot](https://huggingface.co/datasets/lerobot) của chúng ta để bắt đầu với các dự án của riêng bạn.

Here is an example for academic references:
- Original text: **RT-1: Robotics Transformer for Real-World Control at Scale** (2023)  
  Anthony Brohan et al.  
  This paper demonstrates how to apply transformers to real-world robot control at scale, showing the power of learning from large and diverse datasets.  
  [arXiv:2212.06817](https://huggingface.co/papers/2212.06817)
- Translation: **RT-1: Robotics Transformer for Real-World Control at Scale** (2023)  
  Anthony Brohan et al.  
  Bài báo này minh chứng cách áp dụng transformer cho việc điều khiển robot thực tế trên quy mô, cho thấy sức mạnh của việc học từ các tập dữ liệu lớn và đa dạng.  
  [arXiv:2212.06817](https://huggingface.co/papers/2212.06817)

If the code block contains many plain texts, prove translation in collapsible <details> tag. Example:
- Original text:
    ```python
    # Simple: current observation → current action
    delta_timestamps = {{
        "observation.images.wrist_camera": [0.0],  # Just current frame
        "action": [0.0]  # Just current action
    }}

    dataset = LeRobotDataset(
        "lerobot/svla_so101_pickplace", 
        delta_timestamps=delta_timestamps
    )
    ```
- Translation (add the <details> collapsible ABOVE of the original code block):
    <details>
    <summary>Bấm để xem bản dịch tiếng Việt</summary>
    ```python
    # Đơn giản: quan sát hiện tại → hành động hiện tại
    delta_timestamps = {{
        "observation.images.wrist_camera": [0.0],  # Chỉ frame hiện tại
        "action": [0.0]  # Chỉ hành động hiện tại
    }}

    dataset = LeRobotDataset(
        "lerobot/svla_so101_pickplace", 
        delta_timestamps=delta_timestamps
    )
    ```
    </details>
    ```python
    # Simple: current observation → current action
    delta_timestamps = {{
        "observation.images.wrist_camera": [0.0],  # Just current frame
        "action": [0.0]  # Just current action
    }}

    dataset = LeRobotDataset(
        "lerobot/svla_so101_pickplace", 
        delta_timestamps=delta_timestamps
    )
    ```

IMPORTANT: 
- Only output the final translated text and nothing else
- Do NOT include any <think> sections, explanations, or step-by-step analysis
- Do NOT show original text alongside translation
- Do NOT include any commentary or instructions
- Just provide the clean, final Vietnamese translation

Please translate the following texts to Vietnamese:

=== BEGIN OF TEXT ===
{content}
=== END OF TEXT ===
'''.strip()

auto_translate(
    prompt=prompt,
    output_lang=output_lang,
)
