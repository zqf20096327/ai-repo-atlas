# AnonymousV73X/SHAMBA-AI

⭐ 14 · HTML · 推送 2026-07-30 · [GitHub](https://github.com/AnonymousV73X/SHAMBA-AI) · [官网](https://sir-alex.surge.sh) · 个人维护

**面向肯尼亚小农户的作物病害拍照诊断平台**

面向肯尼亚小农户的全栈作物病害检测平台：上传叶片照片后数秒内返回病害名称、置信度、严重度、治疗步骤与防治建议。推理采用双引擎——本地 ONNX（MobileNetV2/PlantVillage）优先，Gemini Vision API 兜底并可开放式诊断任意病害；附带基于 Gemini 的追问聊天、PDF 报告导出、英/斯瓦希里语双语界面、匿名扫描与管理后台。覆盖玉米、番茄、羽衣甘蓝、马铃薯、洋葱等作物，界面针对 2G/3G 低端 Android 设备优化。后端 FastAPI + SQLite，前端零框架 HTML/CSS/JS，本地运行需 Python 3.9+ 与 Gemini API key，自带不安全的默认管理员凭据需部署前修改。

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

- 本地 ONNX MobileNetV2 推理 + Gemini Vision API 兜底的双引擎诊断
- 返回病害名称、置信度、严重度、治疗步骤与防治建议
- 英/斯瓦希里语双语 UI，面向 2G/3G 低端 Android 设备优化
- 匿名扫描无需登录，附带 AI 追问聊天与 PDF 报告导出

## 适用场景

- 田间拍叶照快速判断玉米、番茄等作物病害
- 获取治疗步骤、用药建议并导出诊断报告
- 无账号、弱网环境下随时扫描作物

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L31: |🔍 **Instant AI Diagnosis**|Upload a leaf photo → disease name, confidence score & severity in seconds|
> L32: |🧠 **Dual Inference Engine**|Local ONNX (MobileNetV2, PlantVillage) with Gemini Vision API fallback|

## 星数曲线

```mermaid
xychart-beta
    title "AnonymousV73X/SHAMBA-AI 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `96a85fc4c9cc` · [字段定义](../../DATASET.md)*
