# parkpow/deep-license-plate-recognition

⭐ 671 · C++ · MIT · 推送 2026-09-04 · [GitHub](https://github.com/parkpow/deep-license-plate-recognition) · [官网](https://platerecognizer.com/) · 组织维护

**车牌识别服务的示例客户端与运维工具集（不含模型本体）**

ParkPow/Plate Recognizer 官方维护的示例与工具仓库：围绕 Snapshot、Stream、Blur 与 ParkPow 产品，提供图片车牌识别命令行客户端、车牌模糊化/脱敏脚本、FTP/SFTP 批量处理、目录监控与归档、webhook 消费者、道闸继电器控制、性能基准及 C++/C#/Java/Android/Node-RED 等语言示例。仓库本身不含识别模型，需配合 Plate Recognizer 云 API（API token）或自托管 Snapshot SDK 运行，输出含车牌号、置信度与边界框的 JSON。根目录为脚本集合而非可安装包，用 uv 管理开发环境。

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

- 图片车牌识别 CLI：返回车牌号、置信度与边界框 JSON，支持按地区限定
- 车牌模糊化脱敏脚本（高分辨率分图、正则白名单不脱敏）
- FTP/SFTP 批量处理、目录监控归档、webhook 与道闸继电器集成
- 提供 docker/ 目录用于安装管理自托管 Snapshot SDK

## 适用场景

- 快速验证 Plate Recognizer 云 API 或自托管 SDK 的车牌识别效果
- 对图片中的车牌做批量识别或模糊脱敏处理
- 将相机/FTP 服务器的图片接入车牌识别并转发结果到 ParkPow

## 场景标签

`OCR` `目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L3: This repository contains example clients, integrations, and operational utilities
> L5: ParkPow. It does not contain the recognition models themselves.
> L18:  running self-hosted Snapshot SDK

## 星数曲线

```mermaid
xychart-beta
    title "parkpow/deep-license-plate-recognition 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 670 --> 672
    line [671, 671]
```

2026-10-18 671 → 2026-10-25 671（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `5aabc38c5d6a` · [字段定义](../../DATASET.md)*
