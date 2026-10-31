# aymenhmaidiwastaken/reddit-auto-promoter

⭐ 15 · Python · MIT · 推送 2026-03-16 · [GitHub](https://github.com/aymenhmaidiwastaken/reddit-auto-promoter) · 个人维护

**Reddit 营销自动化机器人：本地 Ollama 生成推广评论与帖子**

Python 编写的 Reddit 推广自动化工具：通过 undetected-chromedriver 驱动真实 Chrome 浏览器浏览目标 subreddit，调用本地 Ollama（Llama 3）生成贴合语境的评论与帖子，配合多账号轮换、冷却追踪、浏览器指纹伪装、拟人打字与延迟等反检测措施。内置 3 层质量过滤（100+ 模式检测、关键词相关性、AI 自审），预配置 60+ 目标 subreddit 覆盖 6 个领域，支持自动巡航模式。需 Python 3.8+、Chrome 与本地运行的 Ollama，首次运行需手动登录各账号。README 声明仅供教育用途，自动化交互可能违反 Reddit 服务条款。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 本地 Ollama（Llama 3）生成上下文相关的评论与帖子
- 多账号轮换与浏览器指纹伪装等反检测套件
- 3 层质量过滤：模式检测、关键词相关性、AI 自审
- 预配置 60+ 目标 subreddit，覆盖 6 个领域

## 适用场景

- 在多个 subreddit 自动发布产品推广评论与帖子
- 多账号轮换执行评论、发帖、点赞的定时循环
- 预览 AI 生成内容后再决定是否发布

## 场景标签

`浏览器自动化` · 领域:效率与自动化

## 证据(README 行号)

> L18: - **AI-Powered Content** — Uses local Ollama (Llama 3) to generate context-aware, human-like comments and posts tai
> L32: │  Chrome      │────▶│  Reddit      │────▶│  Ollama (Local) │

## 星数曲线

```mermaid
xychart-beta
    title "aymenhmaidiwastaken/reddit-auto-promoter 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `28abd09ce656` · [字段定义](../../DATASET.md)*
