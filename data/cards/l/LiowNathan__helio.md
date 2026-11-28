# LiowNathan/helio

⭐ 112 · TypeScript · MIT · 推送 2026-11-27 · [GitHub](https://github.com/LiowNathan/helio) · 组织维护

**内嵌 Helius 文档的助手：解答 RPC 调用与流订阅问题**

Helio 是构建在 Helius 文档站内的助手，由编写文档的团队维护，覆盖 RPC 调用与 WebSocket 订阅两个主题，非通用聊天机器人。回答固定由五部分组成：调用方法、完整可复制的请求体、文档引用链接、注意事项、下一步建议；全部内容基于文档索引，页不存在时明确说明而非编造。使用无需账号或安装，执行调用需用户自己的 key；回答超长时折叠正文，偏离主题时拒绝并引导回两个主题。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 回答固定五段结构：调用、请求体、引用、注意事项、下一步
- 答案基于文档索引，随文档同仓同部署更新
- 密钥处理：不存储 key，对含 key 的 URL 提示风险
- 离题提问、无对应文档页、模糊提问均有明确处理行为

## 适用场景

- 快速查某个 Solana RPC 方法的调用方式与请求体
- 排查 WebSocket 订阅断连与重连方案
- 在文档页内直接获取带引用链接的答案

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L23: Helio is our own assistant. It is built and maintained by the team that writes the documentation it reads, and it s
> L25: It answers the two things people actually get stuck on: making an RPC call, and keeping a subscription alive. It is
> L29: Every answer is grounded in the documentation index behind the site. If a page does not exist, the answer says so i


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `556c62019546` · [字段定义](../../DATASET.md)*
