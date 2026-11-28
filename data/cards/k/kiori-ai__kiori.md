# kiori-ai/kiori

⭐ 3 · JavaScript · NOASSERTION · 推送 2026-10-31 · [GitHub](https://github.com/kiori-ai/kiori) · [官网](https://kiori.io) · 组织维护

**为角色 AI 应用提供角色记忆、秘密与关系的存储服务**

面向开发者与角色扮演应用的记忆层服务：接收角色卡或名字+段落描述，生成可由应用持有的大脑（JSON），随对话调用 organize 让角色只学习其见证的内容，recall 以检索方式返回角色当下所知供拼入提示词，另可检查草稿是否泄露其未闻之事。支持任意模型与语言，用户自带模型密钥（OpenRouter/OpenAI/Gemini）。零依赖服务器，约 3,800 行代码；自托管免费限个人与非商业用途，商业使用需商业许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 三次调用完成集成：create/organize/recall，recall 为检索而非生成
- 大脑为 JSON 对象由应用持有，服务端不存大脑与聊天记录
- 提供 JavaScript/Python SDK、OpenAI 兼容 drop-in、SillyTavern 扩展四种接入方式
- 编辑、重掷与删除消息会被识别并反向学习

## 适用场景

- 给聊天应用/游戏中的角色添加逐角色记忆与关系状态
- 群聊场景下让角色只知道其亲历的剧情
- 接入现有 OpenAI 风格客户端为角色补充记忆能力

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L23: Not a chatbot: the mind behind yours. Your app does the talking and your model writes every line. Kiori is the part
> L77: ||**Kiori API**|**SillyTavern extension**|**The drop-in**|**Self-hosted**|
> L130: Settings, the CLI and moving to a server: docs/self-hosting.md and deploy/. Running your own is free for personal 

## 星数曲线

```mermaid
xychart-beta
    title "kiori-ai/kiori 星数(近 2 点)"
    x-axis ["2026-11-26", "2026-11-28"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-26 3 → 2026-11-28 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `694e06d15447` · [字段定义](../../DATASET.md)*
