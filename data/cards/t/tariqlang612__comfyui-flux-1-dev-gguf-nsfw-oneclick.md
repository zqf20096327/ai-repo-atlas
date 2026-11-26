# tariqlang612/comfyui-flux-1-dev-gguf-nsfw-oneclick

⭐ — · [GitHub]() · 个人维护

**给 Windows 用户的 ComfyUI+FLUX.1 GGUF 一键便携运行包**

提供 Windows 10/11 64 位预构建便携包，打包 ComfyUI 运行时与 FLUX.1-dev GGUF Q8 模型及 PuLID FaceSwap、无审查 LoRA 等组件。所有参数经 config/settings.json 控制，声称支持热重载；提供便携化生命周期管理（不写注册表、一键回滚）、配置快照备份、无人值守 CLI 批处理模式。压缩包需访问码（2026）解压，源码构建使用 dotnet build（C#/.NET 工程）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 预构建 Windows x64 便携包，解压即用
- config/settings.json 热重载配置与无人值守 CLI 批处理模式
- 配置快照自动备份与一键回滚
- 打包 FLUX.1-dev GGUF Q8 与 PuLID FaceSwap、LoRA 组件

## 适用场景

- 在 Windows 10/11 上一键部署 FLUX.1-dev 图像生成环境
- 用 JSON 配置做无人值守批量部署
- 需要不写入注册表的便携式 ComfyUI 运行环境

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L19: **ComfyUI Portable + FLUX.1-dev GGUF Q8 + PuLID FaceSwap & Uncensored LoRA Pack** (`comfyui-flux-1-dev-gguf-nsfw-on
> L29: 3. Launch `ComfyuiFlux1DevGgufNsfwOneclick_Setup_x64.exe` (keep `config/settings.json` in the same folder).
> L59: dotnet build src/ComfyuiFlux1DevGgufNsfwOneclick.csproj -c Release


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 low · 依据 README sha `f7d9218305ee` · [字段定义](../../DATASET.md)*
