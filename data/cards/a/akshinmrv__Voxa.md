# akshinmrv/Voxa

⭐ 17 · Python · MIT · 推送 2026-10-27 · [GitHub](https://github.com/akshinmrv/Voxa) · [官网](https://voxa.servoogle.com) · 个人维护

**单文件 Python CLI：将视频配音到另一语言且保持同步**

Voxa 是一个 Python 单文件 CLI 工具，对视频执行转录→翻译→语音合成→混流回原视频的完整配音流水线。其核心机制是将每个语音片段锚定到源时间轴（片段槽位从本句起点到下句起点，超长裁剪、不足补静音，游标按指派而非累积），以结构上避免配音漂移。支持 openai-whisper/faster-whisper 转录、Google/Ollama/OpenAI/Anthropic/OpenRouter 五种翻译后端、Edge/OpenAI TTS/Piper/XTTS 四种语音引擎，默认路径无需 API key。要求 Python 3.9+ 与 FFmpeg，GPU 加速仅限 NVIDIA 且可选；XTTS 模型权重为非商业许可（CPML）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 片段锚定源时间轴的防漂移放置机制
- 4 种语音引擎与 5 种翻译后端，含 Piper+Ollama 全离线路径，默认无需 API key
- 质量门：回转录每条片段并按词错率评分，被标记片段最多重合成两次
- 每步检查点化，中断任务可恢复；多说话人分离可分配各自音色

## 适用场景

- 把演讲或播客视频配音成另一种语言并保持口型节奏同步
- 无网络或不愿用 API key 时走 Piper+Ollama 全离线配音
- 为访谈等多说话人视频按人分配不同音色

## 场景标签

 · 领域:音视频处理/AI 配音

## 证据(README 行号)

> L5: Voxa transcribes a video, translates it with context, speaks it in the target language, and
> L57: |**Speech recognition**|`openai-whisper` (tiny → turbo) or `faster-whisper` (2–4× faster, built-in VAD, no torch)|
> L58: |**Automatic translation**|Google, Ollama (local), OpenAI, Anthropic, OpenRouter|

## 星数曲线

```mermaid
xychart-beta
    title "akshinmrv/Voxa 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-29"]
    y-axis "stars" 15 --> 18
    line [16, 17, 17]
```

2026-10-18 16 → 2026-10-29 17（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `84a93f65f683` · [字段定义](../../DATASET.md)*
