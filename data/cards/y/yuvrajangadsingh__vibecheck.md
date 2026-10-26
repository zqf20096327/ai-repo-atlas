# yuvrajangadsingh/vibecheck

⭐ 27 · TypeScript · NOASSERTION · 推送 2026-09-02 · [GitHub](https://github.com/yuvrajangadsingh/vibecheck) · [官网](https://www.npmjs.com/package/@yuvrajangadsingh/vibecheck) · 个人维护

**检测 AI 生成代码坏味道的 JS/TS 与 Python 静态检查工具**

面向开发者的命令行 linter，自称"AI slop 的 ESLint"：以 40 条规则扫描 JS/TS 与 Python 代码，覆盖硬编码密钥、空 catch、TypeScript any 滥用、幻觉依赖导入、叙述式注释等类别。零配置、零 API key、本地运行，基于规则匹配而非调用模型。提供 npx 直接运行与 macOS/Linux 独立二进制，支持 GitHub Actions 集成、SARIF 输出、diff 模式、基于校准语料的 slop score 评分及 --min-score 构建门禁；许可为 FSL。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 40 条规则覆盖安全/错误处理/AI 特征痕迹等类别，JS/TS 与 Python 双语言
- slop score 评分基于 6 仓库校准语料，公式与校准文件可复现（src/calibration.json）
- diff/--staged 模式只报告变更引入的发现，配合 --fail-on 做 PR 门禁
- 提供 GitHub Actions 集成与 SARIF 2.1.0 输出

## 适用场景

- 在 CI 中用 --min-score 或 --fail-on 拦截 AI 生成代码的坏味道
- PR 审查时用 diff 模式只看本次改动引入的问题
- 扫描幻觉依赖导入与硬编码密钥等安全隐患
- 给代码库算一个 slop score 追踪整体质量漂移

## 场景标签

 · 领域:开发者工具/代码质量

## 证据(README 行号)

> L5: **40 rules for catching AI-generated code smells.** ESLint for AI slop.
> L22: AI coding tools generate code that *works* but cuts corners. Empty catch blocks, hardcoded secrets, `as any` everyw
> L24: vibecheck catches these patterns with zero config, zero API keys, zero cost. Runs locally, stays fast.

## 星数曲线

```mermaid
xychart-beta
    title "yuvrajangadsingh/vibecheck 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-26 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `ba9acc8cb67f` · [字段定义](../../DATASET.md)*
