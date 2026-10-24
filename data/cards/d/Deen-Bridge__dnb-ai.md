# Deen-Bridge/dnb-ai

⭐ 163 · Python · MIT · 推送 2026-10-23 · [GitHub](https://github.com/Deen-Bridge/dnb-ai) · 组织维护

**DeenBridge 平台的伊斯兰知识 AI 服务：FastAPI + Gemini**

Deen Bridge 伊斯兰教育平台三个服务中的 AI 后端：以 Google Gemini 为模型，配合伊斯兰知识系统提示、内容安全过滤与会话历史，提供聊天 API 供前端 Web 应用调用。支持阿拉伯语等多语言、经训结构化引用（校验到 114 章索引）、Tafsir 经典注疏检索、圣训研究（isnad 链分析、传述人交叉引用）、置信度感知回答与学者审核队列、用户长期记忆及语义缓存。另含 Stellar/USDC 相关计算与解码端点，但不签名或提交交易。通过 X-API-Key 认证与三级限流；可 git clone 或 Docker 部署，需 Python 3.11+ 与 Gemini API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 包装 Gemini 的伊斯兰知识聊天 API，含内容安全过滤与会话历史
- Tafsir 注疏检索与圣训研究 agent（isnad 链分析、传述人交叉引用、十大圣训集变体对齐）
- 置信度感知：低置信度弃答/对冲，可疑宗教答案进入学者审核队列
- 每用户长期记忆（含 GET/DELETE 透明端点与 remember 退出选项）与语义缓存

## 适用场景

- 为伊斯兰教育平台的用户提供带经训引用的问答助手
- 按用户购买记录与钱包余额估算 USDC 天课（zakat）
- 由学者通过审核端点复核低置信度的宗教性回答

## 场景标签

`AI 助手` `RAG` · 领域:对话与助手

## 证据(README 行号)

> L14: This service powers the AI assistant inside **Deen Bridge**, a platform for authentic Islamic education built on th
> L39: - 🕵️ **Hadith Research Agent** — retrieval, isnad chain analysis, rijal (narrator) cross-referencing, grading justi
> L49: |`POST`|`/chat`|Start or continue a chat session|


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `b924bdf9d991` · [字段定义](../../DATASET.md)*
