# merakeen/gitmeup

⭐ 21 · Python · NOASSERTION · 推送 2026-02-21 · [GitHub](https://github.com/merakeen/gitmeup) · [官网](https://pypi.org/project/gitmeup/) · 个人维护

**开发者 CLI：用 Gemini 将 git 变更整理为原子提交命令**

面向开发者的命令行工具：收集 git status 与 git diff 上下文（排除图片、lockfile、压缩产物以控制 token），发送给 Gemini（默认 gemini-2.5-flash-lite，经 google-genai 接入，需 API key），返回按 Conventional Commits 1.0.0 规范分批的 git add / git commit 命令计划。默认 dry-run 不执行，需 --apply 才运行；不生成任何 push 或远程操作，执行前校验提交头格式并规范路径引号与大小写。通过 PyPI 安装，支持 ~/.gitmeup.env 与环境变量配置。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- LLM 将变更分组为原子语义提交并生成 git add/commit 命令
- 默认 dry-run 模式，--apply 显式执行，不执行任何 push
- 上下文清洗：排除图片、lockfile、压缩资产以控制 token
- Conventional Commits 头格式校验与 POSIX 严格路径引号

## 适用场景

- 复杂变更后自动拆分为多个语义化原子提交
- 按 Conventional Commits 规范生成提交信息
- 处理含空格/特殊字符路径的暂存命令生成

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L3: `gitmeup` leverages popular LLMs to organize changes into atomic, semantic batches, and generates precise `git add` 
> L41: This sanitized context is transmitted to an LLM model _(default: Gemini)_, which returns a single code block contai
> L44: - Corresponding `git commit -m "..."` commands following the Conventional Commits specification.

## 星数曲线

```mermaid
xychart-beta
    title "merakeen/gitmeup 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-29 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `17b627b3a32c` · [字段定义](../../DATASET.md)*
