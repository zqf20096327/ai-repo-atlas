# microsoft/evolving-intent

⭐ 30 · Python · MIT · 推送 2026-07-24 · [GitHub](https://github.com/microsoft/evolving-intent) · [官网](https://arxiv.org/abs/2607.20734) · 组织维护

**研究框架：把静态基准转为意图演变的多轮对话并评测 LLM**

Microsoft Research 的研究项目代码库：将 GSM8K、BIRD-SQL、BrowseComp+、SWE-Bench Verified 等静态基准分解为函数与参数，经反事实扩展与情境模拟生成意图逐步披露、修正、切换的多轮对话，再以 OpenAI/Azure OpenAI API 运行评测与多模型对比。提供 DataLoader 式的用户模拟接口，支持确定性评测模式与训练随机采样模式，可通过 --naturalizer_model 在线改写对话轮次。以 conda 环境与 Python 脚本形式运行，面向 LLM 评测研究人员。

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

- 五阶段流水线：意图抽取→反事实/前驱扩展→情境模拟→评测
- 5 种对话场景（fully-specified/argument-reveal/argument-revision/function-switch/combined）
- DataLoader 式接口，评测模式确定性、训练模式随机采样
- 支持 GSM8K/BIRD-SQL/BrowseComp+/SWE-Bench Verified 四类基准

## 适用场景

- 研究 LLM 在多轮对话中跟踪演变意图的能力
- 把现有静态基准改造为动态多轮评测环境
- 生成带意图演变的多轮对话训练数据

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L13: This work studies how well LLMs track and act on
> L111: |5|`evaluation/`|Run models, score answers, analyze results|

## 星数曲线

```mermaid
xychart-beta
    title "microsoft/evolving-intent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 29 --> 31
    line [30, 30]
```

2026-10-18 30 → 2026-10-28 30（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `7b6c16ce51a2` · [字段定义](../../DATASET.md)*
