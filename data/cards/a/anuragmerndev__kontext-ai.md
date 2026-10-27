# anuragmerndev/kontext-ai

⭐ 25 · TypeScript · MIT · 推送 2026-07-03 · [GitHub](https://github.com/anuragmerndev/kontext-ai) · 个人维护

**在 ChatGPT 与 Claude 间一键迁移对话上下文的 Chrome 扩展**

Manifest V3 Chrome 扩展：通过平台自身会话 API 完整捕获 ChatGPT 或 Claude 对话（非 DOM 抓取），生成结构化交接内容并自动填入目标 AI 的输入框，从不自动发送。摘要由 Chrome 内置 Gemini Nano 在本地生成，可选 BYOK（OpenAI/Anthropic/Gemini/OpenRouter），无引擎时保留原文转录。本地优先：无账号、无服务器、无遥测。需 Chrome 128+，源码构建加载。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 重放平台会话 API 实现全保真捕获（仅当前分支、全部回合）
- Gemini Nano 设备端摘要，长对话 map-reduce 适配上下文
- 摘要引擎回退链：Nano → BYOK 四家 → 原文转录
- 本地库保存全部 kontext：搜索、查看、重新摘要、导出原文

## 适用场景

- 达到消息上限后把 ChatGPT 对话连同上下文迁移到 Claude（或反向）
- 在多个 AI 工具间积累并复用可移植的对话记忆
- 隐私敏感用户希望全程本地处理、无遥测的对话迁移

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L7: Capture any ChatGPT or Claude chat, distill it into a portable *kontext*, and continue it in the other — local-first
> L54: |🧠|**On-device summaries**|Chrome's built-in Gemini Nano runs the summary locally — free, private, no key. Long cha
> L104: - **Raw fallback** — if no engine is available, the kontext keeps the full transcript and the handoff uses that. N

## 星数曲线

```mermaid
xychart-beta
    title "anuragmerndev/kontext-ai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-27 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `65f96c54d3c8` · [字段定义](../../DATASET.md)*
