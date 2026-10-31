# Kibertum/tausik-core

⭐ 19 · Python · Apache-2.0 · 推送 2026-10-23 · [GitHub](https://github.com/Kibertum/tausik-core) · [官网](https://tausik.tech) · 个人维护 · 中文 README

**AI 编码代理的验证与控制层：无证据不得关闭任务**

运行在 Claude Code、Cursor、Codex 等 AI 编码代理之上的验证层。代理必须先以验收标准开启任务才能改代码，必须出示通过检查的证据并附 ed25519 签名回执（绑定 commit、可离线验证）才能关闭任务；钩子在编辑阶段直接拦截而非拦截 PR。含项目记忆（SQLite 记录决策与失败尝试）、151 个 MCP 工具、23 个实时钩子、25 套按技术栈的验证套件。需 Python 3.11+ 与 git，以 git submodule 加 bootstrap 脚本安装。声明不防故意绕过、不省 token。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- QG-0/QG-2 双检查点：无验收标准不得开工，无通过检查不得收工
- ed25519 签名回执绑定 commit，可离线用公钥验证
- 23 个实时钩子含任务门、bash 防火墙、push 门、自动格式化
- 项目记忆与共享知识库存于本地 SQLite，跨会话加载

## 适用场景

- 要求 AI 代理在收工前出示真实通过的测试与审查证据
- 阻止代理未经任务定义就大范围修改代码
- 记录失败尝试，避免代理反复走同样的弯路

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L9: TAUSIK sits on top of the AI coding agent you already use — Claude Code, Cursor, Codex and others — and checks its w
> L11: **Where it sits.** The field calls this discipline *harness engineering*: a harness is the agent loop, the tool int

## 星数曲线

```mermaid
xychart-beta
    title "Kibertum/tausik-core 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-31 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `c98d9eb32d1c` · [字段定义](../../DATASET.md)*
