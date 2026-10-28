# vdeng-ai/ComfyUI-MiVolo-V2

⭐ 29 · Python · CC-BY-SA-4.0 · 推送 2026-09-17 · [GitHub](https://github.com/vdeng-ai/ComfyUI-MiVolo-V2) · 个人维护 · 中文 README

**ComfyUI 节点：用 MiVolo V2 模型预测图像中人物的年龄与性别**

对 iitolstykh/mivolo_v2 模型（Transformer、人脸+人体多输入）的 ComfyUI 封装节点：接收图像，经 YOLO 检测器（可选）定位人脸与人体后，输出年龄数值与性别字符串，支持多人（逗号分隔）。模型权重支持 Hugging Face 自动下载或手动放置，仅支持 MiVOLO v2，FaceAge ClientScan 与 MiVOLO-Next 仅为未来候选后端。限制：batch 输入只处理首张图；模型以 trust_remote_code=True 加载，需信任来源。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | CC-BY-SA-4.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 人脸+人体多输入的年龄与性别预测，多人输出逗号分隔字符串
- MiVOLO 与 YOLO 检测模型均支持自动下载或手动离线放置
- README 附 LAGENDA 基准指标表与候选模型可用性评估
- 要求 Python 3.10+，依赖版本范围有界

## 适用场景

- 在 ComfyUI 工作流中对输入图像做年龄/性别预测
- 分析 AI 生成人像的年龄性别属性
- 基于年龄/性别条件控制后续生成流程

## 场景标签

`人脸识别` · 领域:感知与多模态

## 证据(README 行号)

> L8: Use the advanced **MiVolo V2** model directly in ComfyUI for high-precision age and gender prediction!
> L10: This project is a ComfyUI wrapper node for the `iitolstykh/mivolo_v2` model. MiVolo is a Transformer-based, multi-i
> L14: * **Age Estimation:** Receives an image (containing a face or body) and outputs the predicted age as a string.

## 星数曲线

```mermaid
xychart-beta
    title "vdeng-ai/ComfyUI-MiVolo-V2 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-28 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `81215c97b2df` · [字段定义](../../DATASET.md)*
