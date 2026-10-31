# hanbinhsh/SD-LoRA-Manager

⭐ 34 · C++ · MIT · 推送 2026-10-25 · [GitHub](https://github.com/hanbinhsh/SD-LoRA-Manager) · 个人维护 · 中文 README

**本地 Stable Diffusion LoRA 模型与返图管理桌面工具**

C++ & Qt 构建的 Windows 桌面应用，面向本地 SD 生态用户：按 SHA256 哈希自动匹配 Civitai 拉取元数据、封面与触发词，管理多个 LoRA 目录与收藏夹；扫描本地输出目录，解析 PNG 生成信息、统计 Tag 并支持中英翻译；通过本地 Ollama 或 LM Studio API 调用大模型改写提示词（人物/服装替换、偏好生成），内置 WD14 反推（需自有 Python/SD 环境）。提供 .exe 直接运行，源码构建需 Qt 6.2+、CMake 与 OpenSSL 开发库。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 按文件哈希自动匹配 Civitai 拉取封面、简介、触发词
- 本地返图扫描、PNG Info 解析与 Tag 频率统计/中英翻译
- 调用本地 Ollama / LM Studio 大模型辅助提示词生成
- 多 LoRA 目录、收藏夹、多维度筛选与本地离线缓存

## 适用场景

- 无需启动 WebUI 即可浏览、筛选和管理本地 LoRA 库
- 查看某 LoRA 在本地返图中的实际使用情况与 Tag 统计
- 借助本地大模型改写或生成符合个人习惯的提示词

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L3: 一个优雅、高（？）性能的本地Stable Diffusion 模型(主要是LoRA模型)管理、图库管理和提示词辅助工具。（主要围绕Civitai元数据与本地SD生态设计，联网同步Civitai时国内需要魔法）
> L5: 专为解决本地模型混乱、预览图缺失、元数据难以查看、本地返图管理难而设计。无需启动WebUI，即可快速浏览、筛选和管理你的LoRA库及生成的图片，也可以直接调用本地大模型辅助改写提示词。
> L53: * **Ollama / LM Studio 支持**：可选择本地 Ollama 或 OpenAI 兼容的 LM Studio API，调用本地大模型辅助提示词生成。

## 星数曲线

```mermaid
xychart-beta
    title "hanbinhsh/SD-LoRA-Manager 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-28", "2026-10-31"]
    y-axis "stars" 32 --> 35
    line [33, 34, 34]
```

2026-10-18 33 → 2026-10-31 34（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `8c9ce9f5932e` · [字段定义](../../DATASET.md)*
