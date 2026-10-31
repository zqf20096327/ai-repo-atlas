# luxus/pi-xai

⭐ 14 · TypeScript · MIT · 推送 2026-08-13 · [GitHub](https://github.com/luxus/pi-xai) · 个人维护

**为 Pi 终端 agent 接入 xAI/Grok 订阅的扩展包**

TypeScript 编写的 Pi（≥0.80）扩展：通过 Grok Build 订阅的 cli-chat-proxy 端点与 OAuth 登录，为 Pi 提供 xAI 模型目录（grok-4.6 等 8 个模型）、图像生成/编辑、图生视频、web_fetch、goal/plan 模式、下一提示预测、订阅用量显示与纯文本模型的视觉路由等工具。也可切换到公开 api.x.ai 端点（OAuth 或 XAI_API_KEY）。以 pi install npm:pi-xai 安装，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Grok Build 订阅 OAuth 登录 + 模型目录（8 个 Grok 模型，最长 2M 上下文）
- 图像生成/编辑与图生视频工具（image_gen / image_edit / image_to_video）
- goal / plan 模式、下一提示预测（prompt ghost）、订阅用量状态栏
- web_fetch（含 SSRF 阻断）与多 agent 研究工具

## 适用场景

- 在 Pi 终端 agent 中使用 Grok 订阅额度调用 xAI 模型
- 通过 /imagine、/imagine-video 命令生成图片和视频
- 查看 Grok 订阅剩余用量并跟踪目标/计划执行

## 场景标签

`图像生成` `视频生成` · 领域:内容生成

## 证据(README 行号)

> L15: **Today:** Grok Build provider path for Pi (subscription **cli-chat-proxy**, OAuth, model catalog, payload/header p
> L5:  xAI / Grok extras for Pi
> L32: pi install npm:pi-xai

## 星数曲线

```mermaid
xychart-beta
    title "luxus/pi-xai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `c7cc630603c7` · [字段定义](../../DATASET.md)*
