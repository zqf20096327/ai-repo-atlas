# Rexoplanets/layout-studio-moss-image-comfy-node

⭐ 5 · HTML · GPL-3.0 · 推送 2026-11-22 · [GitHub](https://github.com/Rexoplanets/layout-studio-moss-image-comfy-node) · [官网](https://rexoplanets.github.io/layout-studio-moss-image/Layout_Studio_for_MOSS_Image.html) · 个人维护

**为 MOSS-Image 用户可视化绘制 bbox 布局提示词的 ComfyUI 节点**

面向 ComfyUI 的 MOSS-Image 专用布局编辑节点：在拖放画布上绘制 text/object/character 类型 bounding box，自动换算到 MOSS-Image 的 yxyx 居中坐标系（-500 至 500）并满足 16 像素倍数约束，导出 JSON 提示词接入正向提示节点；也支持导入现有 JSON 或带元数据 PNG 反向编辑，可另导出自然语言或 Danbooru 标签格式的纯文本提示。单文件 HTML、本地运行、无外部网络调用。需 ComfyUI 环境与 ≥2.5 CFG 生成参数。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 拖放画布直接生成符合 MOSS-Image 模式（schema）的 JSON bbox 提示词
- 支持 9 种宽高比与 ~1-4 MP 像素预设，网格对齐 16 像素倍数
- JSON/PNG 元数据导入与多格式（JSON/自然语言/标签）导出
- 单文件 HTML 架构，无外部服务器或网络调用

## 适用场景

- 为 MOSS-Image 多角色场景绘制 bbox 布局，避免角色特征混合
- 为海报、专辑封面设计文字与标志位置
- 从已有生成图的 PNG 元数据导入 JSON 继续编辑布局
- 导出纯文本提示词给其他文生图模型做 img2img 或局部重绘（inpainting）

## 场景标签

`图像生成` `提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L3: Take the guesswork out of creating bounding-box layouts for MOSS-Image with this free, open-source, visual spatial-p
> L24: **Use the Studio right in ComfyUI to lay out what you want where**. Just hook the JSON Output to your positive prom
> L180: Released open-source under the GNU GPL v3 Licence. Independent community tool, not affiliated with OpenMOSS.


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `6da38944903b` · [字段定义](../../DATASET.md)*
