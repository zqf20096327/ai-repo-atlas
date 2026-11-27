# MrKyaw/Industrial-Agent-Intelligence

⭐ 3 · Python · MIT · 推送 2026-10-23 · [GitHub](https://github.com/MrKyaw/Industrial-Agent-Intelligence) · 个人维护

**工业设施 AI Agent 行为与认知层参考实现，附确定性评测**

将设施遥测、告警、本体知识与维护文档转化为带证据引用的可审计答案。核心机制包括：数字声明需通过证据账本校验否则阻断、带风险分级与角色的策略化工具注册表、防提示注入的确定性护栏、低置信度与关键告警升级人工，以及 22 个行为评测用例的确定性评测框架（无 LLM-as-judge）。零运行时依赖，纯 Python 3.10+，默认路径无模型推理；数据全为合成数据，作者声明这是作品集/参考实现而非真实产品。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 数字声明对照证据账本校验，未溯源的数字阻断回答
- 策略化工具注册表：风险分级、角色限制、防篡改审计链
- 确定性护栏覆盖未溯源数字、缺引用、不安全写入、陈旧遥测与提示注入
- 22 个行为评测用例与 HTML 评分卡，零运行时依赖

## 适用场景

- 冷机厂房告警风暴的分诊与根因排序并引用遥测证据
- 从对齐数据计算 COP/kW/ton 等能效指标而非依赖仪表盘
- 设定值变更建议经边界校验后路由给工程师确认
- 对 Agent 回答做行为回归测试并在劣化时使 CI 失败

## 场景标签

`模型评测` `RAG` · 领域:评测与运维

## 证据(README 行号)

> L11: A dependency-free reference implementation of the **behavioural and cognitive layer**
> L268: **Does it call an LLM?** No. The reference agent is deterministic. An optional
> L322: - No network calls and no model inference in the default path.


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 mid · 依据 README sha `a5441b372fcf` · [字段定义](../../DATASET.md)*
