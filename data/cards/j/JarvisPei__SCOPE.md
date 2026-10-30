# JarvisPei/SCOPE

⭐ 85 · Python · MIT · 推送 2026-03-26 · [GitHub](https://github.com/JarvisPei/SCOPE) · 组织维护 · 中文 README

**从执行轨迹自动优化 agent 提示词的自进化框架**

SCOPE 是一个自动提示词优化框架：从 agent 执行轨迹中检测错误与质量信号，用 Generator/Selector 双模型合成候选准则并择优，经双流路由（战术记忆存内存、战略记忆落盘）沉淀为可复用规则，再以 θ_new = θ_base ⊕ M_strategic ⊕ M_tactical 的方式演化提示词。面向构建 agent 的开发者，通过 pip 安装为 Python 库，支持 OpenAI、Anthropic 及经 LiteLLM 的 100+ 提供方，可自定义提示模板与领域类别，配套 arXiv 论文。

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

- 从执行轨迹自动合成准则并做 Best-of-N 选择
- 双流记忆：战术（任务级/内存）与战略（跨任务/落盘）
- 记忆自动整合：冲突消解、包含剪枝与合并
- 支持 OpenAI/Anthropic 及 LiteLLM 100+ 提供方，可自定义提示与领域

## 适用场景

- 让我的 agent 在运行中自动积累改进提示词的规则
- 跨任务沉淀战略规则并在初始化时加载复用
- 为个人助理或编码 agent 定制优化领域与模板

## 场景标签

`提示工程` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L5:  A framework for automatic prompt optimization that learns from agent execution traces
> L30: **SCOPE** transforms static agent prompts into self-evolving systems that learn from their own execution. Instead o

## 星数曲线

```mermaid
xychart-beta
    title "JarvisPei/SCOPE 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-30"]
    y-axis "stars" 83 --> 86
    line [84, 85, 85]
```

2026-10-18 84 → 2026-10-30 85（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `bd5cec76fdb3` · [字段定义](../../DATASET.md)*
