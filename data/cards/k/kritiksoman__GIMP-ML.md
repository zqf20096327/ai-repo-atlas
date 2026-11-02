# kritiksoman/GIMP-ML

⭐ 1,559 · Python · MIT · 推送 2026-11-01 · [GitHub](https://github.com/kritiksoman/GIMP-ML) · 个人维护

**GIMP 3 插件：通过外部 API 文生图与文字改图**

面向 GIMP 3.0+ 的图像插件，在 Filters > GIMP-ML 原生对话框中提供三项命令：文本生成图像、编辑选中图层、编辑可见画布。通过 OpenRouter 或 Google 的图像 API 调用 Gemini 等模型，无需本地模型、GPU 或独立 UI。生成结果默认作为新图层插入，替换像素支持撤销；编辑需明确同意上传图像，输入 PNG 限 12 MiB/3200 万像素。macOS 提供 Keychain 密钥管理，凭据也可经 .env 或环境变量配置。安装需 Python 3.10+ 并运行 install.py。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三项命令：文生图、编辑选中图层、编辑可见画布
- 连接 OpenRouter 或 Google 图像 API，无需本地模型或 GPU
- 结果默认作为新图层，替换像素支持单步撤销
- macOS Keychain 存储密钥；编辑需显式同意上传

## 适用场景

- 在 GIMP 内用文字提示生成新图像图层
- 用文字描述修改现有图层或整幅画布
- 在图像编辑工作流中调用 Gemini 图像模型

## 场景标签

 · 领域:图像编辑/生成式 AI 工具

## 证据(README 行号)

> L3: **GIMP-ML brings text-driven image creation and editing directly into GIMP 3.**
> L9: - **Generate Image**: turn a text prompt into a new image or document layer.


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-02 · 置信度 high · 依据 README sha `d05cfec293b9` · [字段定义](../../DATASET.md)*
