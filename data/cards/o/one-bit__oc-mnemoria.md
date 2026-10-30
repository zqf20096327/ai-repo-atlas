# one-bit/oc-mnemoria

⭐ 21 · TypeScript · MIT · 推送 2026-03-02 · [GitHub](https://github.com/one-bit/oc-mnemoria) · [官网](https://www.npmjs.com/package/oc-mnemoria) · 个人维护

**OpenCode 多 agent 共享持久记忆插件，基于 mnemoria Rust 引擎**

为 OpenCode 各 agent（plan/build/ask/review）提供共享持久记忆存储：每条记忆标注来源 agent，跨会话保留上下文。底层为 mnemoria Rust 引擎，采用追加式二进制日志存储，支持 BM25+语义混合检索、CRC32 校验链与损坏恢复，完全本地离线运行。插件通过 chat.message 钩子自动提取用户意图、在会话开始时向系统提示注入跨 agent 上下文，并提供 7 个工具与 /mn-* 斜杠命令；也可通过 mnemoria CLI 直接检索、导出、校验与压缩存储。需 Rust 工具链、OpenCode v0.1+ 与 Node.js >=18，安装脚本一键配置。

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

- 多 agent 共享单一持久记忆库，条目标注来源 agent
- BM25+语义混合检索，亚毫秒级搜索延迟（<10k 条目）
- 追加式二进制日志 + CRC32 校验链，支持 verify 完整性检查与损坏恢复
- 两步维护流程（forget 墓碑标记 + compact 压缩），可提交到 Git 版本控制

## 适用场景

- 让规划、构建、审查等 agent 之间共享决策与发现，不丢失上下文
- 跨会话回忆以往用户目标与技术决策
- 在 CI 或 pre-commit 中校验记忆库完整性
- 通过 CLI 导出 JSON 做脚本分析或数据迁移

## 场景标签

`多智能体` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L24: context from previous conversations. oc-mnemoria fixes this by giving all
> L113: At the start of each session, the plugin injects cross-agent context into

## 星数曲线

```mermaid
xychart-beta
    title "one-bit/oc-mnemoria 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-30 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `7ec66314c794` · [字段定义](../../DATASET.md)*
