# WildEyeConservation/TrapTagger

⭐ 45 · JavaScript · Apache-2.0 · 推送 2026-10-30 · [GitHub](https://github.com/WildEyeConservation/TrapTagger) · 组织维护

**面向生态学家的红外相机图像 AI 标注与管理 Web 应用**

WildEye Conservation 开发的 Web 应用，用 AI 分类配合人工标注处理红外相机拍摄的海量野生动物图像。内置可识别 55 种南部非洲物种的分类器，训练数据来自与牛津大学 WildCRU 合作整理的逾百万张图像。部署面向 AWS：文档给出 EC2 服务器、VPC 子网隔离、Aurora MySQL/PostgreSQL 数据库、S3 与 IAM 等全套配置步骤；也可改在本地或其他云上运行。第三方分类器置于无外网访问的私有子网中。另提供免费托管账号注册途径。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- AI 自动分类与人工标注混合的工作流
- 内置可识别 55 种南部非洲物种的分类器
- AWS 部署文档覆盖 EC2/VPC/RDS/S3/IAM 配置
- 第三方分类器隔离在无互联网访问的私有子网

## 适用场景

- 生态研究团队批量标注和管理红外相机图像
- 野生动物调查数据的组织与归档
- 在自建 AWS 实例上运行相机陷阱图像处理平台

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L9: Camera traps are an invaluable tool for analysing wildlife populations. However, the sheer amount of data they gener
> L11: TrapTagger allows for a hybridised approach between automatic AI classifications and manual annotations with an eff

## 星数曲线

```mermaid
xychart-beta
    title "WildEyeConservation/TrapTagger 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 44 --> 46
    line [45, 45]
```

2026-10-18 45 → 2026-10-31 45（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `1dc5a96fa727` · [字段定义](../../DATASET.md)*
