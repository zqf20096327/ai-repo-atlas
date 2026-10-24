# mgifford/ACCESSIBILITY.md

⭐ 80 · CSS · MIT · 推送 2026-10-01 · [GitHub](https://github.com/mgifford/ACCESSIBILITY.md) · [官网](https://mgifford.github.io/ACCESSIBILITY.md) · 个人维护

**声明项目无障碍状态的开放格式，为人类与 AI agent 提供统一规范**

类似 SECURITY.md 的开放格式：以人和机器可读的清单声明项目的 WCAG 符合级别、已知障碍、测试过的辅助技术，并约定 issue 标签、合并门槛、严重度矩阵等治理规则。为 AI 编码代理（Copilot、Cursor、Claude 等）提供明确的系统指令与组件级最佳实践，配套 CI 工作流（axe-core/Lighthouse）、pre-commit 钩子、可信来源注册表和 Copilot 引导工作流。采用方式为复制模板与示例文件。README 声明项目仍为实验性，内容多为 AI 辅助生成、未经充分实际验证。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 人与机器可读的无障碍状态清单格式（对齐 AGENTS.md）
- 配套 CI/pre-commit 工作流运行 axe-core 与 Lighthouse 检查
- TRUSTED_SOURCES.yaml 机器可读可信来源注册表，含月度自动维护
- Copilot coding agent 引导工作流可自动填写模板并开草稿 PR

## 适用场景

- 在我的仓库声明无障碍承诺与当前 WCAG 状态
- 让 AI 编码助手遵循无障碍规范生成代码
- 在 CI 中加入无障碍回归检查与合并门槛
- 为 AI 系统提供经过审校的无障碍参考来源

## 场景标签

 · 领域:Web 无障碍/开发治理

## 证据(README 行号)

> L5: Just as `SECURITY.md` defines how to handle vulnerabilities, **`ACCESSIBILITY.md`** defines the inclusive state of a
> L26: 3. **Configure AI agents** → Use AGENTS.md as a guide
> L59: 3. **For AI Agents:** It provides explicit "System Instructions" for LLMs (like Copilot, Cursor, or GPT-4) to ensur

## 星数曲线

```mermaid
xychart-beta
    title "mgifford/ACCESSIBILITY.md 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-24"]
    y-axis "stars" 78 --> 81
    line [79, 80, 80]
```

2026-10-18 79 → 2026-10-24 80（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `2e406d8071de` · [字段定义](../../DATASET.md)*
