# haesleinhuepf/translate-pptx

⭐ 21 · Python · BSD-3-Clause · 推送 2026-10-12 · [GitHub](https://github.com/haesleinhuepf/translate-pptx) · 个人维护

**命令行工具：用 LLM 翻译 PowerPoint PPTX 文件**

Python 命令行工具，读取 PPTX 幻灯片并调用 OpenAI 的 GPT-4o（默认模型）翻译其中文本，借助 python-pptx 处理文件格式，输出翻译后的 PPTX。可通过环境变量指定其他 OpenAI 兼容服务器（如本地或机构服务器）及模型。定位为科研项目，用于多语言培训材料的生成，README 要求用户自行核验生成内容并警告幻灯片数据会被传输至第三方服务器。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 一条命令翻译整个 PPTX 文件（translate-pptx file.pptx german）
- 默认使用 OpenAI GPT-4o，当前仅支持 OpenAI 系 LLM
- 支持通过环境变量接入 OpenAI 兼容的自定义/本地服务器
- 基于 python-pptx 读写 PPTX 文件格式

## 适用场景

- 把讲座或培训幻灯片快速翻译成其他语言
- 科研团队生成多语言培训/教学材料
- 通过自建 OpenAI 兼容服务器翻译含内部内容的幻灯片

## 场景标签

 · 领域:文档处理/翻译工具

## 证据(README 行号)

> L5: translate-pptx is a command line tool that translates PowerPoint PPTX files from one language to another.
> L21: Under the hood it uses OpenAI's GPT-4o to translate the text in the slides and python-pptx to handle the file-forma
> L25: `translate-pptx` is a research project aiming at streamlining generation of multi-lingual training materials. Under

## 星数曲线

```mermaid
xychart-beta
    title "haesleinhuepf/translate-pptx 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-30 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `51791ea0831f` · [字段定义](../../DATASET.md)*
