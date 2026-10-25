# Azornes/Comfyui-Model-Resolver

⭐ 47 · JavaScript · MIT · 推送 2026-10-16 · [GitHub](https://github.com/Azornes/Comfyui-Model-Resolver) · 个人维护

**ComfyUI 扩展：自动定位工作流缺失模型并下载更新路径**

面向 ComfyUI 用户的模型解析扩展：扫描当前工作流引用但在本地缺失的模型，提供忽略大小写与扩展名的本地模糊匹配；无法本地命中时可在 CivitAI、Hugging Face、CivArchive、Lora Manager Archive 及 ComfyUI-Manager 模型数据库中在线搜索（含 SHA256 哈希精确查询），后台异步下载到对应目录，并将解析结果写回工作流节点（含嵌套子图）。提供 Python 与可选 Aria2 两种下载后端及自动的 Hugging Face Xet 传输，支持动态下载路径模板与本地哈希计算。要求 ComfyUI 0.26.0+ 与 Python 3.10+。

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

- 缺失模型的本地模糊匹配与相似度评分
- CivitAI/Hugging Face 等 5 类来源在线搜索与后台下载
- 解析结果写回工作流节点，支持嵌套子图与 LoraManager/rgthree 加载器
- Python/Aria2 双下载后端与自动 Hugging Face Xet 传输

## 适用场景

- 加载他人分享的工作流后一键补齐缺失模型
- 重命名或移动过的模型文件通过哈希与模糊匹配重新关联
- 按 base_model/标签模板自动归档下载的 Lora 与 Checkpoint

## 场景标签

 · 领域:AI 图像生成/模型管理

## 证据(README 行号)

> L3:  Find missing models in ComfyUI, download them from supported sources, and update workflow paths.
> L25: - **Search supported sources.** Find files on CivitAI, Hugging Face, CivArchive, Lora Manager Archive, and the Comf

## 星数曲线

```mermaid
xychart-beta
    title "Azornes/Comfyui-Model-Resolver 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-23", "2026-10-25"]
    y-axis "stars" 40 --> 47
    line [41, 43, 46, 46]
```

2026-10-18 41 → 2026-10-25 46（+5）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `a3ca3135c8e3` · [字段定义](../../DATASET.md)*
