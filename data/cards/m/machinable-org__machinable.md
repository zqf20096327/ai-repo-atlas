# machinable-org/machinable

⭐ 36 · Python · MIT · 推送 2026-10-28 · [GitHub](https://github.com/machinable-org/machinable) · [官网](https://machinable.org) · 组织维护

**面向科研代码的实验管理框架：一次编写、运行即查询**

Python 写的内容寻址研究代码系统：以模块与配置定义实验身份，相同运行自动去重、参数扫描增量执行，结果可从代码直接读取，无需跟踪运行名称或路径。用 get("train", {...}).launch() 启动或用同一接口读回结果。通过 pip 安装，文档见 machinable.org。面向机器学习与数据科学研究者的开发框架，不直接提供模型输出。

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

- 以模块+配置作为运行身份的内容寻址机制
- 相同运行自动去重、参数扫描增量执行
- 运行与读取结果使用同一编程接口

## 适用场景

- 我想管理机器学习实验，避免重复运行相同配置
- 我想从代码直接读取历史实验结果做分析
- 我想做参数扫描并只执行新配置

## 场景标签

`科研工具` `MLOps` · 领域:学习与行业

## 证据(README 行号)

> L8: **machinable** is a content-addressed system for research code. You write an
> L10: them are the same gesture. A run's identity is its module and configuration,

## 星数曲线

```mermaid
xychart-beta
    title "machinable-org/machinable 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 35 --> 37
    line [36, 36]
```

2026-10-18 36 → 2026-10-29 36（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `bd2e40db5a95` · [字段定义](../../DATASET.md)*
