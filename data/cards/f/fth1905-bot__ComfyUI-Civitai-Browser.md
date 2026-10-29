# fth1905-bot/ComfyUI-Civitai-Browser

⭐ 27 · JavaScript · MIT · 推送 2026-10-03 · [GitHub](https://github.com/fth1905-bot/ComfyUI-Civitai-Browser) · 个人维护

**ComfyUI 内浏览 Civitai 工作流与模型并一键配齐的扩展**

ComfyUI 前端+API 扩展，在侧栏增加 Civitai 浏览页：可按类别搜索 Civitai 的工作流与模型，一键将工作流加载到画布，扫描其引用的缺失模型并下载到对应目录，也支持列出缺失自定义节点并经 ComfyUI-Manager 安装。不新增节点、不修改 ComfyUI 核心文件，无需额外 Python 依赖，卸载即删目录。浏览无需 API key，下载部分资源需配置 Civitai API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 一键加载工作流并扫描/下载其缺失模型到正确目录
- 支持多种缺失模型来源：内嵌 URL、Civitai 精确文件名匹配、手动粘贴链接、Use mine 复用已有文件
- 按类型归档下载（checkpoints/loras/vae 等），.civitai_part 临时文件避免半写损坏
- 安全删除规则：仅删本扩展下载且未被其他工作流使用的模型，服务端二次校验

## 适用场景

- 在 ComfyUI 里直接找 Civitai 工作流并配齐所需模型
- 发现工作流缺哪些模型和自定义节点并补齐
- 复用本地已有相似模型避免重复下载

## 场景标签

 · 领域:生成式 AI 工具/图像生成工作流

## 证据(README 行号)

> L14: It adds a **Civitai** tab to the ComfyUI sidebar, next to Templates, Workflows and Models. From there you can searc
> L16: It's a pure frontend + API extension. It **adds no nodes**, **never modifies ComfyUI's core files**, and if it ever

## 星数曲线

```mermaid
xychart-beta
    title "fth1905-bot/ComfyUI-Civitai-Browser 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-29 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `c8c24f78088f` · [字段定义](../../DATASET.md)*
