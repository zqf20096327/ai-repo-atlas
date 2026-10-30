# Ebo1996/green-guardian-ml

⭐ 17 · TypeScript · NOASSERTION · 推送 2026-09-14 · [GitHub](https://github.com/Ebo1996/green-guardian-ml) · [官网](https://green-guardian-five.vercel.app) · 组织维护

**面向农户的植物病害识别与作物推荐 Web 平台**

Next.js + Django + MongoDB 的全栈 Web 平台，内置两个机器学习模型：上传植物照片经 MobileNetV2 CNN 识别 38 类病害（模型自 HuggingFace 首次运行自动下载）；输入土壤与气候参数（N、P、K、pH、降雨等 7 项）由 RandomForest 模型在 22 种作物中推荐（自述 99.5% 准确率）。提供治疗建议报告、CSV/PDF 导出、扫描历史与 API 限流（10 次/小时、20 次/小时）。部署文档针对 Vercel/Railway/Atlas 免费层，README 声明项目为教育与作品集用途。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- MobileNetV2 识别 38 类植物病害，覆盖番茄、马铃薯、玉米等 15 种作物
- RandomForest 作物推荐模型（22 类作物，自述 99.5% 准确率）
- 诊断报告 CSV/PDF 导出与扫描历史记录
- API 限流与图像校验（类型、大小上限 10 MB）

## 适用场景

- 上传植物照片即时获得病害诊断与治疗方案
- 根据土壤与气候参数获得种植作物建议
- 导出和管理历次诊断报告

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L52: - **🦠 Plant Disease Detection** — Upload a photo, get instant diagnosis across **38 disease classes** using MobileN
> L53: - **🌾 Crop Recommendation** — Enter soil parameters (N, P, K, pH, rainfall, etc.), get the best crop suggestion usi

## 星数曲线

```mermaid
xychart-beta
    title "Ebo1996/green-guardian-ml 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 16 --> 18
    line [17, 17]
```

2026-10-18 17 → 2026-10-30 17（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `b91c0c053c32` · [字段定义](../../DATASET.md)*
