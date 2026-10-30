# Hiroki-org/jules-extension

⭐ 21 · TypeScript · MIT · 推送 2026-10-28 · [GitHub](https://github.com/Hiroki-org/jules-extension) · [官网](https://marketplace.visualstudio.com/items?itemName=HirokiMukai.jules-extension) · 组织维护

**VSCode 中操作 Google Jules AI 编程代理的扩展**

VSCode 扩展，通过 Jules API 连接 Google 的 AI 编程代理 Jules：设置并校验 API 密钥（存储于 VSCode SecretStorage），创建编码会话、发送后续消息、审批计划，侧边栏实时查看会话状态，展示执行命令、编辑文件与思考过程的日志，支持打开 diff/changeset、检出分支、打开 PR。可通过 Marketplace 或 VSIX 文件安装，支持 GitHub OAuth 登录。面向使用 Jules 的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- API 密钥管理与校验，密钥存于 VSCode SecretStorage
- 会话创建、跟进消息、计划审批与失败原因查看
- 侧边栏实时会话状态监控与活动日志（命令/文件/思考过程）
- 打开 diff、changeset、检出分支、在浏览器打开 PR

## 适用场景

- 在 VSCode 内直接给 Jules 分派编码任务并跟踪进度
- 审查 Jules 生成的计划与代码变更后合并
- 管理历史 Jules 会话与本地缓存

## 场景标签

`编码 Agent` `代码审查` · 领域:编码与开发

## 证据(README 行号)

> L9: Jules Extension is an extension that allows you to operate Google's AI coding agent **Jules** directly from within V
> L24: |**Set API Key**|On first use, set your API key to connect to your Jules account. The key is stored securely in VSC

## 星数曲线

```mermaid
xychart-beta
    title "Hiroki-org/jules-extension 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-29", "2026-10-30"]
    y-axis "stars" 19 --> 22
    line [20, 21, 21]
```

2026-10-18 20 → 2026-10-30 21（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `931c4cfcdf2b` · [字段定义](../../DATASET.md)*
