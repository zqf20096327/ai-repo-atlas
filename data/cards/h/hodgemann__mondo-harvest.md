# hodgemann/mondo-harvest

⭐ 3 · Python · MIT · 推送 2026-11-11 · [GitHub](https://github.com/hodgemann/mondo-harvest) · 个人维护

**从 AI 生成图像/视频元数据提取提示词并存为 JSON 的 CLI**

一个单文件 Python 命令行工具，扫描文件夹中 AI 生成图像与视频的元数据（ComfyUI 工作流图、PNG text chunks、EXIF、XMP、IPTC、视频标签），提取提示词及其生成参数（模型、LoRA 及强度、负向提示、采样器、种子等），每文件夹输出一份 JSON 收割文件。只读取元数据，不解码图像视频数据，不修改源文件。另有可选步骤可将提取的提示词合并入 Mondocraft 的已存提示词。运行仅需 Python 3.10+，读视频需 PATH 中的 ffprobe。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 沿 ComfyUI 工作流从保存节点回溯到采样器，提取实际使用的提示词
- 识别并剥离 LoRA 触发词与 <lora:…> 标签，按文件名启发式匹配
- 按字段名与文本形态过滤误报，跳过照片/版权类元数据
- 长任务每两分钟保存进度，中断后可续跑

## 适用场景

- 批量整理 ComfyUI 输出文件夹中的提示词档案
- 统计文件夹内各类元数据字段的分布
- 把已生成图像的提示词导入 Mondocraft 工作区复用

## 场景标签

 · 领域:生成式 AI 工具链/元数据处理

## 证据(README 行号)

> L7: Harvest the prompts left inside AI-generated images and videos into a JSON file.
> L9: Point it at a folder of outputs, even one with tens of thousands of files, and it saves one harvest file listing eve
> L10: distinct prompt once, with what made each output: model, LoRAs, negative prompt, sampler settings and seed. Only


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 mid · 依据 README sha `a6bfd69212a7` · [字段定义](../../DATASET.md)*
