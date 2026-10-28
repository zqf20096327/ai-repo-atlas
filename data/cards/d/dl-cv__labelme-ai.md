# dl-cv/labelme-ai

⭐ 43 · Python · NOASSERTION · 推送 2026-10-13 · [GitHub](https://github.com/dl-cv/labelme-ai) · 组织维护 · 中文 README

**基于 LabelMe 深度重开发的图像标注工具，面向数据集构建**

深度视觉 LabelmeAI 是 LabelMe 开源版的 fork，面向图像标注与数据集构建场景。在原版基础上提供：标注内嵌写入 PNG/JPEG/TIFF/BMP/WebP 图片（像素不重新编码）并同时保存外部 JSON、自动保存 JSON、画笔标注、旋转框标注、灰度图转换、标签名称与 RGB 显示、双击改标签、快捷键与右键打开文件夹等。README 另描述了离屏 UI 验收流程（python -m labelme --ui-test 与 pytest）。安装包通过官网链接获取，未给出源码安装命令。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 标注内嵌写入多种图片格式，像素不重新编码
- 画笔、旋转框、灰度图转换等新增标注功能
- 自动保存 JSON，标注文件据称为 5KB-15KB
- 提供离屏截图验收与 pytest 测试流程

## 适用场景

- 构建图像分类/分割等数据集的日常标注工作
- 需要把标注随图片文件一起保存、避免外部 JSON 分离管理的场景
- 在 4K 以上大图之间快速切换标注

## 场景标签

 · 领域:计算机视觉/数据标注

## 证据(README 行号)

> L2: 深度视觉LabelmeAI是一款基于LabelMe开源版进行深度重开发的更加智能的标注工具。这个工具与开源版本相比的不同之处主要在于以下几点， 这些更改让你能够更加轻松的快速构建你的数据集。
> L97: This repo is the fork of labelme

## 星数曲线

```mermaid
xychart-beta
    title "dl-cv/labelme-ai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 41 --> 43
    line [42, 42]
```

2026-10-18 42 → 2026-10-28 42（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `af28ae6f77ed` · [字段定义](../../DATASET.md)*
