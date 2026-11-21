# arm092/autoharness-codex

⭐ 4 · Python · MIT · 推送 2026-10-14 · [GitHub](https://github.com/arm092/autoharness-codex) · 个人维护

**为 Codex CLI 维护自学习技能库的插件**

作为 Codex CLI 的原生插件运行：通过五个钩子从会话转录中提取可复用经验，验证证据来源、合并重复技能、保留可恢复历史，只管理自身知识库。提供 macOS/Windows 安装包（内置 Python 运行时，无需单独安装）与源码安装方式，带 CLI 与十二个 MCP 工具；检索支持英、俄、亚美尼亚、法、西五种语言的技术词匹配，为本地排序而非嵌入服务。后台反思消耗用户的 Codex 模型额度，并有每日 token 预算限制。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 从会话转录提取技能，验证证据并合并重叠条目
- 五钩子+十二个 MCP 工具的原生 Codex 插件集成
- 五语言技术检索与带类型来源溯源（lesson_kind/evidence_ids）
- 每日 token 准入预算与字节上限等可配置项

## 适用场景

- 让 Codex 从已完成会话中沉淀可复用经验
- 检索并查看技能库中已验证的编码教训
- 按版本恢复或整理技能库历史

## 场景标签

`编码 Agent` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L3: A self-maintaining skill library for Codex, inspired by tigerless-labs/autoharness.
> L13: An installed, signed-in Codex CLI with native plugins and hooks. Windows Setup includes its own Python runtime;
> L120: Four packaged skills route these requests to twelve MCP tools.

## 星数曲线

```mermaid
xychart-beta
    title "arm092/autoharness-codex 星数(近 3 点)"
    x-axis ["2026-10-29", "2026-10-30", "2026-11-21"]
    y-axis "stars" 2 --> 5
    line [3, 4, 4]
```

2026-10-29 3 → 2026-11-21 4（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `0d4db671feb5` · [字段定义](../../DATASET.md)*
