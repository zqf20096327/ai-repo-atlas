# EU-ECDC/episomer

⭐ 71 · R · EUPL-1.2 · 推送 2026-05-08 · [GitHub](https://github.com/EU-ECDC/episomer) · 组织维护

**ECDC 社媒疫情早期预警工具：监测贴文趋势并检测异常信号**

欧盟疾控中心（ECDC）基于 epitweetr 开发的 R 包：从社媒 API（当前支持 Bluesky）按主题采集贴文并存储于本地数据库，进行地理定位，按主题与地点聚合关键词、URL、标签；信号检测算法识别超出预期的贴文数量，触发邮件预警。内置 Shiny 交互式 Web 应用，含仪表盘、警报页（可训练机器学习模型做警报分类）、地理标注、数据保护与配置等页面。聚焦传染病，可通过修改主题与关键词扩展到其他领域。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | EUPL-1.2 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 按时间/地点/主题自动监测社媒贴文趋势并检测异常信号
- 从 Bluesky API 采集贴文，本地数据库存储与检索
- 内置 Shiny Web 应用（仪表盘、警报、地理标注、数据保护等五页）
- 支持训练机器学习模型对警报按用户定义类别分类

## 适用场景

- 公共卫生机构对传染病相关社媒信号做早期预警
- 对警报进行过滤、验证与人工研判辅助
- 处理贴文数据的删除请求与匿名化（GDPR 场景）

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L7: `Episomer` has been created by building on `epitweetr` objectives and functionalities. The `episomer` package allows
> L11: The package includes an interactive web application (Shiny app) with five pages: the dashboard, where a user can vi

## 星数曲线

```mermaid
xychart-beta
    title "EU-ECDC/episomer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 70 --> 72
    line [71, 71]
```

2026-10-18 71 → 2026-10-31 71（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `b44df9c19db8` · [字段定义](../../DATASET.md)*
