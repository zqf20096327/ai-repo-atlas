# zebangeth/DirPrint

⭐ 37 · Python · MIT · 推送 2026-02-04 · [GitHub](https://github.com/zebangeth/DirPrint) · [官网](https://pypi.org/project/DirPrint/) · 个人维护

**导出项目目录结构与文件内容的命令行工具，便于分享给 LLM**

DirPrint 是一个 Python 命令行工具，将项目目录以树状结构输出，文件内容以 markdown 代码块嵌入，可导出为文件，用途是为 LLM（ChatGPT、Claude 等）提供代码库上下文以辅助调试开发。支持 ignore/omit 两种过滤模式、glob 匹配、自动遵循 .gitignore、尖号包裹的严格精确匹配，以及可选的逐文件行数统计。通过 pip 或源码安装，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 目录树 + 文件内容（markdown 代码块）一体化输出并可导出文件
- ignore/omit 双模式 + glob + 严格匹配（^pattern^）
- 自动遵循 .gitignore 规则（可关闭）
- 可选的文件/目录行数与占比统计

## 适用场景

- 把整个代码库打包成文本贴给 ChatGPT/Claude 做调试
- 过滤敏感或无关文件后分享项目结构
- 统计项目各文件的行数分布

## 场景标签

 · 领域:开发工具/命令行工具

## 证据(README 行号)

> L9: DirPrint is a command-line tool that streamlines sharing your project's directory structure and file contents with L
> L13: - **Visual Directory Tree:** Get a clear, hierarchical representation of your project's structure.
> L14: - **File Contents Display:** View file contents within the tree, formatted in markdown code blocks.

## 星数曲线

```mermaid
xychart-beta
    title "zebangeth/DirPrint 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 36 --> 38
    line [37, 37]
```

2026-10-18 37 → 2026-10-25 37（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `f33d4be0fcd0` · [字段定义](../../DATASET.md)*
