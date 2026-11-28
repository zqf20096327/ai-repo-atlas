# Sh1vvu/medical-risk-screening-bot

⭐ 15 · HTML · 推送 2026-11-27 · [GitHub](https://github.com/Sh1vvu/medical-risk-screening-bot) · 个人维护

**面向普通用户的 Telegram 糖尿病/心脏病早期风险筛查机器人**

基于 XGBoost 模型的 Telegram 机器人，提供糖尿病与心脏病两项风险筛查问卷：用户通过 /screen 等命令进入对话流程逐题作答，结果显示前回显全部答案供核对，每条结果附带就医提醒。模型优先从 XGBoost 原生 JSON 格式加载并回退到 pickle；启动时做特征-问题映射校验，缺失即拒绝启动。筛查模块各自独立，通过注册新模块即可扩展。README 明确声明这是筛查辅助而非诊断工具，部分临床参数在代码中以 # ASSUMED 标注为假设值。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 糖尿病与心脏病两项 XGBoost 风险筛查问卷
- 结果前回显全部答案，支持 /resume 恢复中断会话
- 启动时校验模型特征与问题映射，缺失字段拒绝启动
- 新增筛查只需一个模块加一条注册项，无需改核心流程

## 适用场景

- 给自己做糖尿病或心脏病的早期风险筛查
- 学习多模型筛查机器人的模块化结构
- 部署自己的 Telegram 筛查机器人实例

## 场景标签

 · 领域:医疗健康/风险筛查

## 证据(README 行号)

> L7: Medical Risk Screening Bot brings multi-model early risk screening for diabetes and heart disease straight into Tele
> L42: **`/screen`** — jump straight into a screening session. Presents the available risk modules (diabetes, heart diseas
> L94: Not at all — and it never claims to be. This is a student machine-learning project built for early, informal risk *


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `344a540167e7` · [字段定义](../../DATASET.md)*
