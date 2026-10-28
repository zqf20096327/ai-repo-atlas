# huggingface/leaderboards

⭐ 25 · 推送 2026-10-14 · [GitHub](https://github.com/huggingface/leaderboards) · 组织维护

**Hugging Face leaderboards 文档仓库：构建与预览文档**

huggingface 组织下的 leaderboards 仓库，README 仅包含文档构建说明：通过 pip 安装 watchdog 与 doc-builder 工具，使用 doc-builder 命令构建 docs/source/en 下的文档到指定目录并以非 Python 模块方式预览。README 未提供关于仓库内容、功能定位或使用者的更多描述，推断其托管 Hugging Face 排行榜相关文档源文件，面向参与 Hugging Face 文档维护的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 提供基于 doc-builder 的文档构建命令
- 提供文档本地预览命令
- 安装依赖为 watchdog 与 huggingface/doc-builder

## 适用场景

- 本地构建与预览 Hugging Face leaderboards 文档
- 参与该仓库文档的修改与校对

## 场景标签

 · 领域:AI 基础设施/文档

## 证据(README 行号)

> L4: pip install watchdog git+https://github.com/huggingface/doc-builder.git
> L10: doc-builder build leaderboard docs/source/en --build_dir build_dir --not_python_module

## 星数曲线

```mermaid
xychart-beta
    title "huggingface/leaderboards 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-28"]
    y-axis "stars" 23 --> 26
    line [24, 25, 25]
```

2026-10-18 24 → 2026-10-28 25（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 low · 依据 README sha `ad4450c792f4` · [字段定义](../../DATASET.md)*
