# AISquare-Studio/AISquare-Studio-QA

⭐ 168 · Python · Apache-2.0 · 推送 2026-10-26 · [GitHub](https://github.com/AISquare-Studio/AISquare-Studio-QA) · 组织维护

**GitHub Action：把 PR 中的自然语言测试描述自动生成并执行 Playwright 测试**

以 GitHub Action 形式部署的自动化 QA 工具：开发者在 PR 描述的 autoqa 代码块中用自然语言编写编号测试步骤，Action 在 PR 事件触发后解析元数据（flow_name/tier/area），由 CrewAI 多智能体（Planner/Executor/Step Executor）生成 Playwright Python 测试代码，经 AST 安全校验后在隔离浏览器上下文中执行，成功后提交到目标仓库并回贴 PR 评论与截图。生成依赖 OpenAI GPT-4 API key 与 staging 环境，也提供本地 Python 3.11+ 运行入口。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自然语言步骤→Playwright Python 测试的生成、执行与提交
- CrewAI 多智能体编排（Planner/Executor/Step Executor）
- AST 安全校验：拦截 eval/exec/subprocess 等危险构造，限制可用 import
- 三种执行模式（generate/suite/all）与 ETag 幂等去重

## 适用场景

- 在 PR 中用英文描述测试步骤，自动生成并运行浏览器测试
- 对新功能即时补充回归测试并归档到 tests/autoqa 目录
- 在 CI 中以 suite 模式回归运行已生成的测试套件

## 场景标签

`多智能体` `浏览器自动化` `代码生成` · 领域:Agent 开发

## 证据(README 行号)

> L10: **AI-powered GitHub Action that converts natural language test descriptions in pull request bodies into fully autom
> L37: 4. CrewAI agents generate Playwright Python test code from the steps
> L194: AutoQA uses a multi-agent architecture powered by CrewAI:

## 星数曲线

```mermaid
xychart-beta
    title "AISquare-Studio/AISquare-Studio-QA 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 167 --> 169
    line [168, 168]
```

2026-10-18 168 → 2026-10-28 168（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `6041984210ef` · [字段定义](../../DATASET.md)*
