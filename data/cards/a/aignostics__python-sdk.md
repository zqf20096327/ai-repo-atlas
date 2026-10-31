# aignostics/python-sdk

⭐ 14 · Python · MIT · 推送 2026-10-30 · [GitHub](https://github.com/aignostics/python-sdk) · [官网](https://aignostics.readthedocs.io) · 组织维护

**已弃用的 Aignostics 计算病理学平台 Python SDK 客户端**

提供访问 Aignostics Platform 云服务的多接口客户端：桌面应用 Launchpad、CLI、示例 Notebook 与 Python 客户端库。平台对全切片病理图像（WSI）运行机器学习分析应用（如 HETA 肿瘤微环境分析），输出 QuPath GeoJSON、TIFF 热图与 CSV 测量数据，单批最多 500 张切片，结果 30 天后自动删除。需组织级商业协议注册并强制 2FA。本 SDK 已声明弃用，仅提供错误与安全修复至 2027-04-30，官方建议迁移至平台 REST API 或 Console。

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

- 桌面应用/CLI/Python 库/REST API 多种接入方式
- 支持 DICOM、TIFF、SVS 全切片图像，单批最多 500 张
- 结果输出 QuPath GeoJSON、TIFF 热图与 CSV，按切片增量交付
- 已弃用：仅修复至 2027-04-30，建议迁移至 REST API/Console

## 适用场景

- 通过 Python 脚本或 Notebook 将病理切片分析接入自有流程
- 批量提交全切片图像并按切片获取分析结果
- 已在用该 SDK 的团队按官方指引迁移到平台 REST API

## 场景标签

 · 领域:医学影像/计算病理学

## 证据(README 行号)

> L28: The **Aignostics Platform** runs computational pathology applications — such as HETA, which analyzes the tumor micr
> L79: The **Aignostics Platform** is a comprehensive cloud-based service that allows organizations to leverage advanced c

## 星数曲线

```mermaid
xychart-beta
    title "aignostics/python-sdk 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `13228533fffe` · [字段定义](../../DATASET.md)*
