# soapbox-pub/shakespeare

⭐ 25 · TypeScript · AGPL-3.0 · 推送 2026-10-23 · [GitHub](https://github.com/soapbox-pub/shakespeare) · [官网](https://shakespeare.diy) · 组织维护

**在浏览器中构建和部署 AI 应用的开源构建器**

完全在浏览器内运行的 React PWA：文件存于 IndexedDB（LightningFS），浏览器直连 AI 提供商与 git 服务（isomorphic-git），支持多提供商（OpenAI、Anthropic、OpenRouter、xAI、Deepseek 等）配置，配置存于 localStorage；用 esbuild-wasm 在浏览器内编译，专化为 TypeScript React 项目，仅兼容项目可直接预览。无后端（仅 services/ 下少数可配置微服务），支持 Nostr/Lightning 匿名购买额度与礼品卡兑换。AGPLv3 许可，提供三个镜像 URL。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 完全浏览器内运行，代码与配置存储于本地（IndexedDB/localStorage）
- 支持 OpenAI、Anthropic、OpenRouter、xAI、Deepseek 等多个 AI 提供商
- esbuild-wasm 在浏览器内编译 TypeScript React 项目
- Nostr/Lightning 匿名购买额度与礼品卡兑换

## 适用场景

- 不依赖后端环境，在浏览器中编写并预览 AI 应用
- 跨设备通过 git 推拉代码同步工作
- 匿名购买 AI 使用额度

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L5: Shakespeare is an open-source AI app builder that runs entirely in your browser.
> L18: Shakespeare is a React PWA that stores files in IndexedDB with LightningFS. Your browser connects directly to AI pr

## 星数曲线

```mermaid
xychart-beta
    title "soapbox-pub/shakespeare 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-30"]
    y-axis "stars" 23 --> 26
    line [24, 25, 25]
```

2026-10-18 24 → 2026-10-30 25（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `ce1c25e9ff28` · [字段定义](../../DATASET.md)*
