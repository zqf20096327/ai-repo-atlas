# naseridev/orven

⭐ 14 · TypeScript · GPL-3.0 · 推送 2026-07-30 · [GitHub](https://github.com/naseridev/orven) · [官网](https://npmjs.com/package/@naseridev/orven) · 个人维护

**面向 AI 编程助手的 MCP 上下文分页与代码知识记录系统**

实现 Model Context Protocol 的本地服务：一方面把项目解析为符号签名索引（tree-sitter/WebAssembly），按需加载函数体、跟踪并回收上下文帧，模拟操作系统内存分页模型以控制上下文窗口占用；另一方面将关于代码的声明（intent/invariant/observation 等）记录为带出处与有效性条件的 claim，随代码变更自动重验证，以内容寻址记录形式存于 .orven/theory/ 并随 git 提交、跨分支合并收敛。任何 MCP 客户端均可接入，提供 CLI 与 15 个 MCP 工具。需要 Node.js 22.13+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三级上下文模型：签名索引、按需加载帧、swap 目录，LRU 驱逐
- claim 生命周期（proposed/active/stale/refuted）绑定符号身份与内容指纹，随代码变更自动重验证
- 理论记录内容寻址、只追加日志，经 git merge 跨分支收敛
- MCP 服务器暴露 15 个工具，客户端无关，纯本地文件运行

## 适用场景

- 让编程助手在大型代码库中导航而不耗尽上下文窗口
- 把函数意图、不变式等知识持久化并在代码变更时重新验证
- 跨会话、跨分支保留并合并团队对代码的已验证认知

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L3: Orven is an MCP-compatible context and memory system for AI-assisted development. It does two connected jobs:
> L8: Orven implements the Model Context Protocol and nothing else. Any editor, assistant, or agent that speaks MCP can co

## 星数曲线

```mermaid
xychart-beta
    title "naseridev/orven 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `69513fe6baa7` · [字段定义](../../DATASET.md)*
