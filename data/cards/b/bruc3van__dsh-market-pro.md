# bruc3van/dsh-market-pro

⭐ 11 · TypeScript · MIT · 推送 2026-11-25 · [GitHub](https://github.com/bruc3van/dsh-market-pro) · [官网](https://dsh-market-pro.com) · 个人维护 · 中文 README

**DeepSeek Harness 的 AI 原生插件·技能·MCP 市场**

作为 DeepSeek Harness（DSH）的第三方市场插件，聚合每日核实的社区插件目录（29,000+）、100 个精选 Agent 技能与 100 个精选 MCP 服务器，提供界面化的浏览、安装、启停、批量更新与卸载管理。安装后自动向会话注册内置技能 /market-pro 与三个工具，用户可在对话中自然语言选型插件/技能/MCP，安装与更新均经宿主原生审批；第三方元数据经防注入处理，密钥以凭据模板引用。可在设置中关闭 AI 助手以回归零常驻 Token。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 对话内 /market-pro 选型：跨插件/技能/MCP 联合检索与去重
- 插件一键批量更新，绑定确认过的精确包名与版本并强制原生审批
- 精选技能免 npx 直装，GitHub 失败自动回退 jsDelivr 镜像
- 第三方元数据防注入（Unicode 剥离 + 边界隔离）与零明文密钥凭据模板

## 适用场景

- 在 DSH 里对话式查找并安全安装插件、技能和 MCP
- 批量检查并更新已安装的 DSH 插件版本
- 粘贴 Claude/Cursor 风格 JSON 快速导入并托管 MCP 配置
- 安装插件后让 AI 只读排查联网请求等潜在风险

## 场景标签

 · 领域:AI 生态/插件与 MCP 市场

## 证据(README 行号)

> L14: > **DSH Market Pro** is an AI-native plugin, Agent Skills, and MCP marketplace for **DeepSeek Harness (DSH)** — fea
> L22: - **面向 Agent 的 AI 原生选型与批量更新（统一内置 Skill `/market-pro` + 插件 · 技能 · MCP 三大工具）**：
> L16: DeepSeek Harness（DSH）的 AI 原生第三方插件市场（官网与在线目录：dsh-market-pro.com）。基于每日核实的社区目录 awesome-dsh-plugin-pro（覆盖 29,000+ 社区插件）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 mid · 依据 README sha `425b69d2e404` · [字段定义](../../DATASET.md)*
