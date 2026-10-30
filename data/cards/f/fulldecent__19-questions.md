# fulldecent/19-questions

⭐ 16 · PHP · MIT · 推送 2026-10-10 · [GitHub](https://github.com/fulldecent/19-questions) · 个人维护

**通过问答进行贝叶斯推断猜测对象的游戏网站**

PHP 实现的网页版“20 个问题”猜物游戏：从历史玩家的问答记录中估计对象与谓词之间的关联，用无偏最大似然估计计算每个候选对象的似然并估计熵，选择期望最小化熵的问题继续提问，在 19 问内猜中即获胜。安装方式为用 SCHEMA.sql 建 SQL 数据库、配置 config.php、上传文件到服务器；可运行 harvestfrom20q 从其他服务器采集初始数据。面向想自部署该游戏的用户，提供在线 demo。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于玩家历史回答的无偏最大似然估计对象似然
- 以熵最小化为准则选择下一个问题
- 支持从其他 20q 服务器采集初始数据（harvestfrom20q）
- 提供 SCHEMA.sql 建库与 PHP 配置文件的自部署流程

## 适用场景

- 自部署一个网页版猜物问答游戏
- 研究熵最小化提问策略的贝叶斯推断实现
- 通过在线 demo 直接游玩

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L21: The program uses statistical inference to estimate which object you are thinking of based on answers you provide. T
> L27: The player’s history of answers are compared against other player’s past responses to questions. We use an unbiased

## 星数曲线

```mermaid
xychart-beta
    title "fulldecent/19-questions 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `a472606d3ce5` · [字段定义](../../DATASET.md)*
