# Glockevonpavlov/synapse-enforcer-leet

⭐ 15 · Python · Apache-2.0 · 推送 2026-08-16 · [GitHub](https://github.com/Glockevonpavlov/synapse-enforcer-leet) · 个人维护 · 中文 README

**用本地 LLM 思维模式编译 LEET 语言理解级高难题组的研究者管线**

面向韩国 LEET 语言理解考试的高难度阅读理解 지문·문항 세트生成管线：输入由 Claude 起草的事实表，本地 LLM（Gemma4-31B-it，思维模式）以每集约 10 次调用生成文章与题目，再经确定性门链（轴分配、代码 lint、集合检测、靶向修补）组装成可供人工快速审核的题组。核心发现是 31B 模型能生成 6/6 反方最优解读却 0/6 正确判定，故生成与验证分离，判定由人完成。引擎仅用 Python 标准库，需一台 vLLM 服务器（验证环境 2× RTX PRO 6000）。目前仅支持语言理解科目。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 사고-네이티브路径：全集约 10 次调用，本地 31B 约 7 分钟
- 确定性门链（轴分配+槽位强制→代码lint→集合检测→靶向修补）恢复集合纪律
- 三模型同框架基准（本地 31B / 本地 250B-MoE / 前沿 API）
- 引擎仅用 Python 标准库，零外部依赖；提供网页运行器与 HWPX 韩文排版输出

## 适用场景

- 生成高难度 LEET 语言理解阅读题组供人工终审
- 在相同框架下对比不同模型出题能力
- 将题组排版为韩文 HWPX 文档

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L8: > **English abstract** — Synapse Enforcer is a thinking-native pipeline that compiles
> L21: > rather than bottlenecking it. Every run is seeded by a **fact sheet** — dry fact
> L79: 요구: Python 3.10+ (엔진은 표준 라이브러리만 사용), vLLM 서버 1대 (검증 환경: 2× RTX PRO 6000, 2×96 GB).

## 星数曲线

```mermaid
xychart-beta
    title "Glockevonpavlov/synapse-enforcer-leet 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `c1ee8fc78c26` · [字段定义](../../DATASET.md)*
