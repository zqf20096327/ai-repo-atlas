# MrHacker-X/ImagineX

⭐ 18 · Python · BSL-1.0 · 推送 2026-10-16 · [GitHub](https://github.com/MrHacker-X/ImagineX) · 个人维护

**个人用 Telegram AI 机器人：问答与文生图两个命令**

基于 python-telegram-bot 21+ 的异步 Telegram 机器人，通过 OpenAI SDK v1+ 提供 /ask 问答（默认 gpt-4o-mini，Chat Completions）与 /gen 文生图（Images API，DALL·E，默认 512x512）。面向个人账号使用，明确声明不支持商业部署或群组场景。配置集中在 config.py，支持环境变量覆盖；依赖仅 4 个包，克隆仓库填入 OpenAI key 与 bot token 后运行 imaginex.py 即可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | BSL-1.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- /ask 问答与 /gen 文生图两个核心命令
- python-telegram-bot 21+ 全异步事件循环
- config.py 单文件配置，环境变量可覆盖
- 缺失凭据时快速失败并给出明确错误

## 适用场景

- 在个人 Telegram 账号上随时提问和生成图片
- 自部署一个轻量的 AI 问答与文生图机器人

## 场景标签

`聊天机器人` `图像生成` · 领域:对话与助手

## 证据(README 行号)

> L25: |1️⃣|`/ask <question>`|Sends your question to an OpenAI chat model and replies with the answer|
> L26: |2️⃣|`/gen <prompt>`|Turns a text prompt into an image via the OpenAI images API and sends it as a photo|
> L71: |🎨|**Image generation**|`/gen` returns a DALL·E image as a Telegram photo - no links to open|

## 星数曲线

```mermaid
xychart-beta
    title "MrHacker-X/ImagineX 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-30 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `591eb5698734` · [字段定义](../../DATASET.md)*
