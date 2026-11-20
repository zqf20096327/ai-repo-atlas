# chrisribe/simple-memory-mcp

⭐ 10 · TypeScript · MIT · 推送 2026-04-17 · [GitHub](https://github.com/chrisribe/simple-memory-mcp) · 个人维护

**给 AI 助手提供跨会话持久记忆的本地 MCP 服务器**

基于 SQLite 的 MCP 服务器，让 AI 助手在会话之间存储与检索信息：关键词全文检索（BM25 相关性评分）、标签组织、JSON 导出/导入备份，可同步到 OneDrive/Dropbox。零配置默认写入 ~/.simple-memory/memory.db，无需向量数据库与嵌入模型，可离线运行。通过 npx 配置 Claude Desktop/VS Code 等任意 MCP 客户端使用，另提供 CLI（setup、search、stats、export/import）。作者声明项目不再是主要维护重心，后续迭代转移到 git-memory。

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

- 本地 SQLite 存储的持久记忆，关键词全文检索与 BM25 评分
- MCP 工具（memory-graphql/export-memory/import-memory）供 AI 自动调用
- npx setup 自动配置 VS Code 与 Claude Desktop，可选 CLI 安装
- 自动备份到 OneDrive/Dropbox，支持自定义数据库路径

## 适用场景

- 让 AI 助手记住我的技术栈偏好与项目决策，跨会话复用
- 把工作中的问题与解决方案存入个人记忆库随时检索
- 离线、无云端依赖地保存个人知识，避免向量库维护成本

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L7: Give your AI assistant persistent memory across sessions.
> L14: **The solution:** Simple Memory lets AI store and retrieve information that persists forever. Local SQLite database
> L98: > 💡 **Best Experience**: Works best with **Claude Sonnet in Agent Mode** for optimal auto-capture.


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 high · 依据 README sha `9252a6a8e5e0` · [字段定义](../../DATASET.md)*
