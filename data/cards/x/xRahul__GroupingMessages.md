# xRahul/GroupingMessages

⭐ 20 · Java · Apache-2.0 · 推送 2026-08-26 · [GitHub](https://github.com/xRahul/GroupingMessages) · [官网](https://github.com/xRahul/GroupingMessages/releases/latest) · 个人维护

**自动将短信归入自定义类别的 Android 应用（端侧学习）**

面向普通用户的 Android 短信管理应用：通过混合端侧分类器（词级 TF-IDF 余弦相似度 + 字符三元组相似度）将收到的短信自动归入用户自定义的带颜色类别，未匹配的消息落入 Unknown。模型按用户训练：把消息移入正确类别即可训练，后续持续从纠正中学习，并可将纠正传播到已存储的相似消息。所有读取、训练与分类均在设备本地完成，无外部 API，唯一网络调用是可选的版本检查。支持 SQLite 数据库备份导出/导入，需自行用 Gradle 构建，最低支持 Android 7.0。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 混合端侧分类器：词 TF-IDF 余弦 + 字符三元组相似度
- 按用户训练并持续从纠正中学习，可回溯传播到已存消息
- 全部短信处理在设备本地，无外部 API 与分析上报
- SQLite 数据库整体备份导出/原子化导入

## 适用场景

- 把杂乱的短信收件箱自动整理进自定义类别
- 按类别查看未读数并一键标记已读
- 离线备份和恢复短信数据库

## 场景标签

 · 领域:移动应用/个人效率

## 证据(README 行号)

> L9: An Android app that automatically categorizes your SMS into categories of your choice.
> L23: - Automatic categorization of incoming SMS using a hybrid on-device classifier

## 星数曲线

```mermaid
xychart-beta
    title "xRahul/GroupingMessages 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-28 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `88a219702827` · [字段定义](../../DATASET.md)*
