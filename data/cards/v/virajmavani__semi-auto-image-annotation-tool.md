# virajmavani/semi-auto-image-annotation-tool

⭐ 596 · Python · Apache-2.0 · 推送 2026-04-18 · [GitHub](https://github.com/virajmavani/semi-auto-image-annotation-tool) · [官网](https://virajmavani.com/annomage) · 个人维护

**半自动图像标注工具：用目标检测模型给出标注建议**

基于 PyTorch 目标检测模型的半自动图像标注工具 Anno-Mage，按用户自定义标签对图像生成检测框建议供人工确认修改，支持 OWL-v2 开放词汇零样本检测。提供两种界面：PyPI 安装后自动在浏览器打开的应用，以及 FastAPI + React 的 Web 应用（后端 8000 端口、前端 3000 端口，可用启动脚本）。输出统一为 CSV（image_path,x1,y1,x2,y2,label）与 Pascal VOC XML 两种格式，注释保存在 ~/.anno-mage/annotations/。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 PyTorch 目标检测模型生成标注建议
- 支持 OWL-v2 开放词汇零样本检测
- 输出 CSV 与 Pascal VOC XML 两种标注格式
- PyPI 包与 FastAPI + React Web 应用两种使用方式

## 适用场景

- 为训练数据集快速预标注图像
- 用自定义标签半自动标注目标检测数据
- 导出 CSV/Pascal VOC 格式标注用于模型训练

## 场景标签

 · 领域:计算机视觉/数据标注

## 证据(README 行号)

> L11: Semi-automatic image annotation toolbox powered by PyTorch object detection models, including open-vocabulary zero-
> L74: ## Output Formats

## 星数曲线

```mermaid
xychart-beta
    title "virajmavani/semi-auto-image-annotation-tool 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 595 --> 597
    line [596, 596]
```

2026-10-18 596 → 2026-10-22 596（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `37b91e19e643` · [字段定义](../../DATASET.md)*
