# nikhileshmeher0204/ScanMyFood

⭐ 39 · Dart · 推送 2026-08-13 · [GitHub](https://github.com/nikhileshmeher0204/ScanMyFood) · 个人维护

**拍照扫描食品标签或菜品并做 AI 营养分析的移动应用**

Flutter 移动端 + Spring Boot 后端的营养分析平台：用户用相机拍摄产品标签或整餐，后端调用 Google Cloud Vertex AI（Gemini 2.0 Flash）提取营养成分并识别食物，提供个性化仪表盘、营养历史记录、健康档案与 Firebase 认证的跨设备云同步。部署需自行搭建 PostgreSQL 14+、JDK 17+ 后端与 Flutter 3.4.3+ 前端，并配置 GCP Vertex AI 与 Firebase 项目，无预编译安装包。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 相机扫描食品标签或菜品，Gemini 2.0 Flash 提取营养成分
- 每日宏量/微量营养摄入仪表盘与历史记录
- 基于个人健康指标与饮食偏好的定制洞察
- Firebase Auth 认证与跨设备云同步

## 适用场景

- 扫描食品标签了解营养成分是否符合我的饮食目标
- 记录并追踪每日营养摄入历史
- 为有特定健康指标的用户获取个性化饮食建议

## 场景标签

`多模态` · 领域:感知与多模态

## 证据(README 行号)

> L18: Built with **Flutter** and **Spring Boot**, leveraging **Google Cloud's Vertex AI (Gemini 2.0 Flash)**, ScanMyFood 
> L23: - **🔍 AI Analysis**: Powered by Gemini 2.0 Flash for accurate nutritional extraction and food identification.

## 星数曲线

```mermaid
xychart-beta
    title "nikhileshmeher0204/ScanMyFood 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 38 --> 40
    line [39, 39]
```

2026-10-18 39 → 2026-10-26 39（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `5593289a07f3` · [字段定义](../../DATASET.md)*
