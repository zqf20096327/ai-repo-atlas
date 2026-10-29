# sawrus/agent-guides

⭐ 19 · Python · MIT · 推送 2026-10-28 · [GitHub](https://github.com/sawrus/agent-guides) · [官网](https://sawrus.github.io/agent-guides) · 组织维护

**为多款编码 agent 统一项目规则与质量门禁的配置包**

面向同时使用多个编码 agent（Codex、Claude Code、OpenCode 等）的团队：提供一套共享项目规则（64 条规则、16 个专业化方向）、在 agent 停止时运行 make test/lint 并记录验收结果的质量门禁、生产/数据库/密钥防护，以及可选的角色团队与工作流、模型路由。通过 npx 交互式安装器写入各 agent 的原生文件，agentic upgrade 保持同步且保留用户修改。默认 lean 配置常驻上下文不超过 2,110 tokens，仅含一个只读 explorer 辅助 agent。

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

- 64 条规则覆盖 16 个软件/DevOps 专业化方向，按 paths 按需加载
- 质量门禁运行测试/lint 并在 .agentic/gate/last.json 记录验收结果
- 生产/数据库/密钥/强制推送等防护守则
- 单一安装覆盖 Codex/Claude Code/OpenCode 实测及 Antigravity/Gemini/Cursor 等配置

## 适用场景

- 团队统一多个编码 agent 的行为规则与完成标准
- 在 agent 停止时自动跑检查并留验收记录
- 接入公司内部规范并随升级自动重放
- 防止 agent 误操作生产环境与非本地数据库

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L3: > One set of project rules for Claude Code, Codex and OpenCode. A quality gate runs your checks and records acceptan
> L33: - ✅ **A gate decides "done".** When the agent stops, the quality gate runs `make test` and `make lint` (or your
> L37: - 🔁 **Install once, keep in sync.** `agentic install` writes the native files of each agent. `agentic upgrade`

## 星数曲线

```mermaid
xychart-beta
    title "sawrus/agent-guides 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-29 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `f5a024c34e2d` · [字段定义](../../DATASET.md)*
