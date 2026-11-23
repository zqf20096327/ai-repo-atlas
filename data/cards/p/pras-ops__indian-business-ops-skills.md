# pras-ops/indian-business-ops-skills

⭐ — · [GitHub]() · 个人维护

**面向印度企业合规运营的 Claude Agent 技能包（GST/TDS/工资/ROC）**

一组遵循 SKILL.md 格式的 agent 技能包，覆盖印度公司合规运营：GST 申报、TDS/TCS、工资法定项目（EPF/ESI/PT）、MCA/ROC 年度申报、注册登记、发票/e-invoice 与 Tally 数据操作。设计原则是模型负责判断、捆绑的 Python 脚本负责精确计算（GSTIN/PAN 校验、CGST/SGST/IGST 拆分），变动税率与截止日期运行时到官方门户确认而非硬编码。含路由技能、确定性评测（17/17 过 CI）、隐私遮蔽提示；明确声明不构成法律意见，非 CA/CS 替代。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | — |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 7 个技能分 4 组，带 start-here 路由技能分发请求
- 捆绑 Python 助手做 GSTIN 校验与税额拆分，结果可复现
- 税率/门槛/截止日期运行时核验官方门户，引用文件带 last_verified 日期并由 CI 检查 90 天时效
- 提供 Claude Code 插件、.skill 下载、源码复制三种安装方式

## 适用场景

- 初创公司查询需要哪些合规登记并由 agent 分步执行流程
- 录入供应商发票前校验 GSTIN 并计算 CGST/SGST 拆分
- 整理 GSTR-1/3B、TDS 24Q/26Q 申报所需的信息清单
- 在 Tally 与 GST/TDS 申报之间对账

## 场景标签

 · 领域:财税合规/企业运营

## 证据(README 行号)

> L8: Agent Skills that help Claude (or any agent that reads the `SKILL.md` format) run the compliance
> L52: Seven focused skills in four groups, plus a **"start here" router** that points a broad or
> L127: explanation stay with the model. This is the layer *between* an AI agent and the business's

## 星数曲线

```mermaid
xychart-beta
    title "pras-ops/indian-business-ops-skills 星数(近 2 点)"
    x-axis ["2026-11-08", "2026-11-22"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-08 3 → 2026-11-22 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `c6307dc60c2a` · [字段定义](../../DATASET.md)*
