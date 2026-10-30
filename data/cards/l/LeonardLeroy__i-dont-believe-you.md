# LeonardLeroy/i-dont-believe-you

⭐ 18 · TypeScript · MIT · 推送 2026-09-24 · [GitHub](https://github.com/LeonardLeroy/i-dont-believe-you) · 个人维护

**让编码 agent 用命令验证 diff 才能声称测试通过的技能**

面向 Claude Code 等编码 agent 的 SKILL.md 技能：要求 agent 在声称测试通过前，对真实 diff 运行八条 git/grep shell 命令并粘贴输出，任一命令有输出即不得声称成功。八项检查覆盖跳过测试、永真断言、删除断言/测试文件、吞异常、伪造测试声明等。无依赖、无 API key、无模型，仅一个 markdown 文件；可设 IDBY_BASE 固定基线防止 agent 提交后绕过；另附可选 CLI 作为 CI 门禁。支持 Codex、Cursor、opencode 等（见 INSTALL.md）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 八条 git/grep 命令强制 agent 粘贴真实输出后才可声称成功
- 无依赖、无 API key、无模型，单个 markdown 文件
- 可选 CLI 在 CI 中运行同样检查
- 可通过一条正则扩展新的测试框架

## 适用场景

- 防止编码 agent 跳过或删除断言后谎称测试通过
- 在 CI 中以独立门禁复核 agent 产出的测试改动
- 为不同测试框架自定义检查规则

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L13: mkdir -p .claude/skills/verify-before-claiming && curl -sL https://raw.githubusercontent.com/LeonardLeroy/i-dont-be
> L20: Before your agent can tell you anything passed, it has to run eight shell commands against the real

## 星数曲线

```mermaid
xychart-beta
    title "LeonardLeroy/i-dont-believe-you 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-30 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `46dced718ce2` · [字段定义](../../DATASET.md)*
