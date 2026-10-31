# RiggdAI/uniqent

⭐ 15 · TypeScript · Apache-2.0 · 推送 2026-10-17 · [GitHub](https://github.com/RiggdAI/uniqent) · [官网](https://uniqent.ai) · 组织维护

**AI agent "大脑"打包与跨框架安装的开放标准与工具链**

Uniqent 定义 .uniqent 开放捆绑包格式，把 agent 的 persona、MCP 栈、技能、记忆与配置打包为单个 Ed25519 签名文件（fail-closed 密钥扫描保证不含密钥），再通过各框架适配器安装到 Claude Code、Hermes、OpenClaw。提供 npx 一键试用 CLI、Tauri 桌面可视化构建器 Studio、Obsidian vault 导入与运行中 agent 导出。面向构建和分发可移植 agent 的开发者；项目自述为 pre-1.0 状态。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- .uniqent 签名捆绑包格式（Ed25519 + 密钥扫描，不含密钥）
- 适配器将大脑翻译为 Claude Code/Hermes/OpenClaw 原生布局并报告转换损失
- Tauri 桌面可视化构建器 Studio 与记忆知识图谱
- Obsidian vault 导入与 CLI（try/install/export/pack/sign）

## 适用场景

- 把一个 agent 的完整配置打包分享给其他框架用户
- 一键安装现成的 featured brain 到本地 agent
- 把 Obsidian 第二大脑转为可携带的 agent 大脑

## 场景标签

`Agent 框架` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L36: unit for "a whole agent." Uniqent makes that unit and the workflow around it: **build → package →
> L39: secrets**. Anyone installs it into the framework they run; a per-framework **adapter** translates
> L72: 4. **Install** it: the adapter verifies the signature, shows a permission sheet, resolves _your_

## 星数曲线

```mermaid
xychart-beta
    title "RiggdAI/uniqent 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-31"]
    y-axis "stars" 13 --> 16
    line [14, 15, 15]
```

2026-10-18 14 → 2026-10-31 15（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `5b854cb89f10` · [字段定义](../../DATASET.md)*
